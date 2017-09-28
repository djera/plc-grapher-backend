from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import EventSerializer
from .models import Event
from rest_framework import filters
from .filters import EventFilter

class RootView(views.APIView):
    """
    Root endpoint - use one of sub endpoints.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    urls_mapping = {
        'events': 'events-list',
    }
    urls_extra_mapping = None

    def get_urls_mapping(self, **kwargs):
        mapping = self.urls_mapping.copy()
        mapping.update(kwargs)
        # if self.urls_extra_mapping:
        #    mapping.update(self.urls_extra_mapping)
        # mapping.update(settings.get('ROOT_VIEW_URLS_MAPPING'))
        return mapping

    def get(self, request, format=None):
        print(request)
        return Response(
            dict([(key, reverse(url_name, request=request, format=format))
                  for key, url_name in self.get_urls_mapping().items()])
        )


class EventViewset(viewsets.ModelViewSet):
    filter_class = EventFilter
    permission_classes = ( permissions.IsAuthenticated, )
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('added_at',)
    ordering = ('-added_at',)