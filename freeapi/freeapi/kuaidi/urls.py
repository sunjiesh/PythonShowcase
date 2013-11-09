#coding=utf-8

from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'search', views.search, name='search'), 
)
