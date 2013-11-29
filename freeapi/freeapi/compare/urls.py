#coding=utf-8

from django.conf.urls import patterns,  url

import views

urlpatterns = patterns('',
    url(r'/param', views.param, name='param'), 
    url(r'^/?$', views.index, name='index'),
)
