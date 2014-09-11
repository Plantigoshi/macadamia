from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^api/', include('Profiles.urls')),
                       url(r'^admin/', include(admin.site.urls)),)
