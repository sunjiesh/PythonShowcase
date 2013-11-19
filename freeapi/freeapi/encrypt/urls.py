#coding=utf-8

from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'genmd5', views.genmd5, name='genmd5'), 
    url(r'md5', views.md5, name='md5'),
    
)
