from authentication import views
from django.contrib.auth import get_user_model
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token
from rest_framework.routers import DefaultRouter
from .views import AllUsersViewset
from django.conf.urls import include, url
from rest_framework.authtoken import views as tokenviews

User = get_user_model()

router = DefaultRouter()
router.register(r'all', AllUsersViewset, base_name='all_users')


base_urlpatterns = (
    url(r'^', include(router.urls, namespace='auth')),
    url(r'^me/$', views.UserView.as_view(), name='user'),
    url(r'^password/$', views.SetPasswordView.as_view(), name='set_password'),
    url(r'^password/reset/$',
        views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password/reset/confirm/$',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    url(r'^login/$', tokenviews.obtain_auth_token, name='login'),
    url(r'^$',
        views.RootView.as_view(
            urls_extra_mapping={'login': 'login', 'logout': 'logout'}),
        name='root'),
    url(r'^login-token-verify/', verify_jwt_token),
    url(r'^login-token-refresh/', refresh_jwt_token),
    url(r'^add/$', views.RegistrationView.as_view(), name='add'),
    url(r'^update/(?P<id>[0-9]+)/$', views.UserView.as_view(), name='update'),
)

urlpatterns = base_urlpatterns + (
    url(r'^$', views.RootView.as_view(), name='root'),)
