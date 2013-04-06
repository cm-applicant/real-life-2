from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^submit$', views.submit, name='submit'),
    url(r'^moderate/(?P<id>\d*)/$', views.moderate, name='moderate'),
)
