from django.conf.urls import patterns, include, url

from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .views import ProfileViewSet
from .views import FriendshipViewSet
from Farms.views import PlantSpe


profile_router = routers.SimpleRouter()
profile_router.register(r'profiles', ProfileViewSet)

friendship_router = nested_routers.NestedSimpleRouter(profile_router,
                                                      r'profiles',
                                                      lookup='profile')
friendship_router.register(r'friends',
                           FriendshipViewSet,
                           base_name='friendship')

urlpatterns = patterns('',
                       url(r'^', include('Farms.urls')),
                       url(r'^', include(profile_router.urls)),
                       url(r'^', include(friendship_router.urls)), )
