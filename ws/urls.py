
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers
#from rest_framework.documentation import include_docs_urls

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from wide_sight.views import APIRoot, viewer, sequencesViewSet, panoramasViewSet, image_object_typesViewSet, image_objectsViewSet
router = routers.DefaultRouter()
router.register(r'sequences', sequencesViewSet)
router.register(r'panoramas', panoramasViewSet)
router.register(r'image_object_types', image_object_typesViewSet)
router.register(r'image_objects', image_objectsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^viewer/$', viewer, name='viewer'),
    url(r'^viewer/([-\w]+)/$', viewer, name='viewer'),
    url(r'^$', APIRoot.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
