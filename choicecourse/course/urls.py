# /bin/bash python
# -*- coding:utf-8 -*-
# author: Jiejing Shan

from django.conf.urls import url

from . import views

app_name = 'course'

urlpatterns = [
    url(r'^index.html$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'course/(?P<pk>[0-9]+)/&', views.DetailViews.as_view(), name='detail'),
]