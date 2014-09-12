from django.conf.urls import patterns, include, url

from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views import ProfileViewSet


profile_router = routers.SimpleRouter()
profile_router.register(r'profiles', ProfileViewSet)

urlpatterns = patterns('',
                       url(r'^', include('Farms.urls')),
                       url(r'^', include(profile_router.urls)),)
