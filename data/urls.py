from django.conf.urls import url
from .views import DataViewset, RootView
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

router = DefaultRouter()
router.register(r'data', DataViewset)

base_urlpatterns = (
    url(r'^', include(router.urls, namespace='data')),
)

urlpatterns = base_urlpatterns + (url(r'^$', RootView.as_view(), name='root'),)
