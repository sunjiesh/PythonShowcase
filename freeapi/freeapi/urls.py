from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^kuaidi', include('freeapi.kuaidi.urls')),
    url(r'^encrypt', include('freeapi.encrypt.urls')),
    url(r'^compare', include('freeapi.compare.urls')),
    url(r'^$', views.index, name='index'),
)
