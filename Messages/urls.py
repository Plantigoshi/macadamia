from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from Plants.urls import user_plant_router
from Plants.urls import plant_router

from .views import VariableViewSet


user_variable_router = routers.NestedSimpleRouter(user_plant_router,
                                                  r'user-plants',
                                                  lookup='user-plant')
user_variable_outer.register(r'variables',
                             VariableViewSet,
                             base-name='user-variables' )


user_value_router = routers.NestedSimpleRouter(user_variable_router,
                                               r'variables',
                                               lookup='variable' )
user_value_router.register(r'values',
                           VariableViewSet,
                           base-name='values' )

variable_router = routers.NestedSimpleRouter(plant_router,
                                             r'plants',
                                             lookup='plant')
variable_router.register(r'variables',
                        VariableViewSet,
                        base-name='variables' )

value_router = routers.NestedSimpleRouter(variable_router,
                                          r'variables',
                                          lookup='variable' )
value_router.register(r'values',
                      VariableViewSet,
                      base-name='values' )

urlpatterns = patterns('',
                       url(r'^', include(user_variable_outer.urls)),
                       url(r'^', include(user_value_router.urls)),
                       urls(r'^', include(variable_router.urls)),
                       urls(r'^', include(value_router.urls)), )
