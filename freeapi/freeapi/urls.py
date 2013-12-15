from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^kuaidi', include('freeapi.kuaidi.urls')),
    url(r'^encrypt', include('freeapi.encrypt.urls')),
    url(r'^compare', include('freeapi.compare.urls')),
    url(r'^api', include('freeapi.api.urls')),
    url(r'^/?$', views.index, name='index'),
)
handler500 = 'freeapi.views.custom_500_view'
handler404 = 'freeapi.views.custom_404_view'
handler403 = 'freeapi.views.custom_403_view'
handler400 = 'freeapi.views.custom_400_view'
