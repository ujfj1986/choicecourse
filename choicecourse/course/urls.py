# /bin/bash python
# -*- coding:utf-8 -*-
# author: Jiejing Shan

from django.conf.urls import url

from . import views
from .view_creator import create_index_view

app_name = 'course'

urlpatterns = [
    url(r'^index.html$', create_index_view(app_name), name='index'),
    url(r'^$', create_index_view(app_name), name='index'),
    url(r'course/(?P<pk>[0-9]+)/&', views.DetailViews.as_view(), name='detail'),
]