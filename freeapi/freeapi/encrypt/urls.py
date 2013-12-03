#coding=utf-8

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'/genmd5', views.genmd5, name='genmd5'), 
    url(r'/crashmd5/(\w{32})', views.crashmd5, name='crashmd5'),
    url(r'/md5', views.md5, name='md5'),    
    url(r'/?$', views.index, name='index'),
)
