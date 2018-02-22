#!/bin/bash python3
# -*- coding: utf-8 -*-
# author: Jiejing Shan
# date: 2018-02-22

from .views import CourseIndexView

def create_index_view(name):
    if name == 'course':
        return CourseIndexView.as_view()
    pass