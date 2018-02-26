#!/bin/bash python3
# -*- coding: utf-8 -*-
# author: Jiejing Shan
# date: 2018-02-22

from .views import CourseIndexView
from classinfo.views import ClassInfoIndexView
from teacher.views import TeacherIndexView
from student.views import StudentIndexView
from django.http import Http404

def error_page(request):
    raise Http404('There is no page.')

def create_index_view(name):
    if name == 'course':
        return CourseIndexView.as_view()

    if name == 'classinfo':
        return ClassInfoIndexView.as_view()
    if name == 'teacher':
        return TeacherIndexView.as_view()
    if name == 'student':
        return StudentIndexView.as_view()
    return error_page