from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from .views import FarmViewSet, PlantViewSet
from Profiles.urls import profile_router


farm_router = routers.NestedSimpleRouter(profile_router, r'profiles', lookup='profile')
farm_router.register(r'farms', FarmViewSet, base_name='farm')

plant_router = routers.NestedSimpleRouter(farm_router, r'farms', lookup='farm')
plant_router.register(r'plants', PlantViewSet, base_name='plant')

urlpatterns = patterns('',
                       url(r'^', include(farm_router.urls)),
                       url(r'^', include(plant_router.urls)),)
