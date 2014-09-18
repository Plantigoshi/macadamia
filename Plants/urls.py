from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from Farms.urls import farm_router
from Profiles.urls import profile_router

from .views import PlantViewSet
from .views import UserPlantViewSet


plant_router = routers.NestedSimpleRouter(farm_router,
                                          r'farms',
                                          lookup='farm')
plant_router.register(r'plants',
                      PlantViewSet,
                      base_name='plant')

user_plant_router = routers.NestedSimpleRouter(profile_router,
                                               r'profiles',
                                               lookup='profile')
user_plant_router.register(r'plants',
                           UserPlantViewSet,
                           base_name='user-plant')

urlpatterns = patterns('',
                       url(r'^', include(plant_router.urls)),
                       url(r'^', include(user_plant_router.urls)), )
