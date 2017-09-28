from django.conf.urls import url
from .views import EventViewset, RootView
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

router = DefaultRouter()
router.register(r'events', EventViewset)

base_urlpatterns = (
    url(r'^', include(router.urls, namespace='eventlog')),
)

urlpatterns = base_urlpatterns + (url(r'^$', RootView.as_view(), name='root'),)
