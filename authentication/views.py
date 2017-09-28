from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from rest_framework import (
    generics, permissions, status, response, views, filters)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework.viewsets import ModelViewSet
from . import serializers, settings, utils, signals
from .filters import UsersFilter


User = get_user_model()


class RootView(views.APIView):
    """
    Root endpoint - use one of sub endpoints.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    urls_mapping = {
        'me': 'user',
        'register': 'register',
        'change-password': 'set_password',
        'password-reset': 'password_reset',
        'password-reset-confirm': 'password_reset_confirm',
    }
    urls_extra_mapping = None

    def get_urls_mapping(self, **kwargs):
        mapping = self.urls_mapping.copy()
        mapping.update(kwargs)
        if self.urls_extra_mapping:
            mapping.update(self.urls_extra_mapping)
        mapping.update(settings.get('ROOT_VIEW_URLS_MAPPING'))
        return mapping

    def get(self, request, format=None):
        return Response(
            dict([(key, reverse(url_name, request=request, format=format))
                  for key, url_name in self.get_urls_mapping().items()])
        )


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        response = super(LoginView, self).post(request, *args, **kwargs)

        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            signals.user_sign_in.send(
                sender=self.__class__, user=user, request=self.request)
        return response


class PasswordResetView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to send email to user with password reset link.
    """
    serializer_class = serializers.serializers_manager.get('password_reset')
    permission_classes = (
        permissions.AllowAny,
    )

    _users = None

    def _action(self, serializer):
        for user in self.get_users(serializer.data['email']):
            self.send_password_reset_email(user)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def get_users(self, email):
        if self._users is None:
            active_users = User._default_manager.filter(
                email__iexact=email,
                is_active=True,
            )
            self._users = [u for u in active_users if u.has_usable_password()]
        return self._users

    def send_password_reset_email(self, user):
        email_factory = utils.UserPasswordResetEmailFactory.from_request(
            self.request, user=user)
        email = email_factory.create()
        email.send()


class SetPasswordView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to change user password.
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_serializer_class(self):
        if settings.get('SET_PASSWORD_RETYPE'):
            return serializers.serializers_manager.get('set_password_retype')
        return serializers.serializers_manager.get('set_password')

    def _action(self, serializer):
        self.request.user.set_password(serializer.data['new_password'])
        self.request.user.save()

        if settings.get('LOGOUT_ON_PASSWORD_CHANGE'):
            utils.logout_user(self.request)

        return response.Response(status=status.HTTP_204_NO_CONTENT)


class PasswordResetConfirmView(utils.ActionViewMixin, generics.GenericAPIView):
    """
    Use this endpoint to finish reset password process.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    token_generator = default_token_generator

    def get_serializer_class(self):
        if settings.get('PASSWORD_RESET_CONFIRM_RETYPE'):
            return serializers.serializers_manager.get(
                'password_reset_confirm_retype')
        return serializers.serializers_manager.get('password_reset_confirm')

    def _action(self, serializer):
        serializer.user.set_password(serializer.data['new_password'])
        serializer.user.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = serializers.CustomUserSerializerEvent
    lookup_field = 'id'
    permission_classes = (
        permissions.IsAuthenticated,
    )


class AllUsersViewset(ModelViewSet):
    """
    Use this endpoint to retrieve/update user.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = serializers.CustomUserSerializerEvent
    filter_class = UsersFilter
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CustomUserSerializerEvent
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('created',)
    ordering = ('-created',)


class RegistrationView(generics.CreateAPIView):
    """
    Use this endpoint to register new user.
    """
    serializer_class = serializers.serializers_manager.get('user_registration')
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request)

    def get_email_context(self, user):
        context = super(RegistrationView, self).get_email_context(user)
        return context
