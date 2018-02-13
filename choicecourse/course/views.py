# /bin/bash python
# -*- coding: utf-8 -*-
# author: Jinjing Shan

from django.shortcuts import render
from django.views.generic import ListView
from .models import Students, Course

import logging

logger = logging.getLogger('course.view')

# Create your views here.
class ListViewRow:
    url = ""
    row_str = ""

    def __init__(self):
        self.url = ""
        self.row_str = ""

    def clear(self):
        self.url = ""
        self.row_str = ""

    def __str__(self):
        return self.row_str

class ListViewData:
    absoluteurl = ""
    pk = ""
    rows = []

    def __init__(self):
        self.absoluteurl = ""
        self.pk = ""
        self.rows = []

class IndexView(ListView):
    model = Course
    template_name = 'course/index.html'
    context_object_name = 'context'
    paginate_by = 10

    '''def get(self, request, *args, **kwargs):
        res = super(IndexView, self).get(request, *args, **kwargs)
        self.blogsession.update(request)
        self.blogsession.setToSession(request)
        return res'''

    '''def get_queryset(self):
        students = super(IndexView, self).get_queryset()
        for post in posts:
            post.update_body()
        return posts
    '''

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        courses = Course.objects.all()
        context['cols'] = ["课程名称", "教课老师", "年级", "学生名单", "课时"]
        datas = []
        for course in courses:
            #teachers = course.teachers.all()
            #for teacher in teachers:
            viewData = ListViewData()
            viewData.absoluteurl = course.get_absolute_url()
            viewData.pk = course.pk
            viewRow = ListViewRow()
            viewRow.url = course.get_absolute_url()
            viewRow.row_str = course.name
            viewData.rows.append(viewRow)
            viewRow.clear()
            viewRow.url = course.teacher.get_absolute_url()
            viewRow.row_str = course.teacher.name
            viewData.rows.append(viewRow)
            viewRow.clear()
            viewRow.row_str = course.grade
            viewData.rows.append(viewRow)
            viewRow.clear()
            students = course.students.all()
            if 2 < len(students):
                viewRow.url = course.get_absolute_url()
                viewRow.row_str = "..."
            else :
                viewRow.row_str = str([student.name for student in students])[1:-1]
            viewData.rows.append(viewRow)
            viewRow.clear()
            viewRow.row_str = course.classes
            viewData.rows.append(viewRow)
            viewRow.clear()
            datas.append(viewData)
        context['datas'] = datas
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number: page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0: page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0: page_number - 1]
            right = page_range[page_number: page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            
        data = {
            'left': left,
            'right': right,
            'right_has_more': right_has_more,
            'left_has_more': left_has_more,
            'first': first,
            'last': last,
        }
        return data