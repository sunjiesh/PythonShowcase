#coding=utf-8

from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'md5', views.md5, name='md5'), 
)
