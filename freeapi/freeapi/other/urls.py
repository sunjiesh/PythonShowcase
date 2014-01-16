#coding=utf-8

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
	url(r'^/?$', views.index, name='index'),
	url(r'/random', views.index, name='random'),
)
