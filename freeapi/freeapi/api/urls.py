#coding=utf-8

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'/wallpaper/([\w]*)', views.getWallpaper, name='wallpaper'),
    url(r'/downloadPic', views.downloadPic, name='downloadPic'),
    url(r'/getip', views.getIp, name='getIp'),
)
