# /bin/bash python
# -*- coding:utf-8 -*-
# author: Jiejing Shan

from django.conf.urls import url

from . import views
from course.view_creator import create_index_view

app_name = 'classinfo'

urlpatterns = [
    url(r'^index.html$', create_index_view(app_name), name='index'),
    url(r'^$', create_index_view(app_name), name='index'),
    url(r'(?P<pk>[0-9]+)/&', views.DetailView.as_view(), name='detail'),
]