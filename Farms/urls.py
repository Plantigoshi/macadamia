from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from .views import FarmViewSet
from Profiles.urls import profile_router


farm_router = routers.NestedSimpleRouter(profile_router, r'profiles', lookup='profile')
farm_router.register(r'farms', FarmViewSet, base_name='farm')

urlpatterns = patterns('',
                       url(r'^', include(farm_router.urls)),)
