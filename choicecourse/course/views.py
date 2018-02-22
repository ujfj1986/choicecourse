# /bin/bash python
# -*- coding: utf-8 -*-
# author: Jinjing Shan

from django.shortcuts import render
from django.views.generic import ListView
from .models import Student, Course

import logging

logger = logging.getLogger('course.view')

# Create your views here.
class Element:
    elem_url = ""
    elem_str = ""

    def __init__(self):
        self.elem_url = ""
        self.elem_str = ""

    def clear(self):
        self.elem_url = ""
        self.elem_str = ""

    def __str__(self):
        return self.elem_str

class Row:
    row_url = ""
    pk = ""
    row_num = 1
    elems = []

    def __init__(self):
        self.row_url = ""
        self.pk = ""
        self.elems = []
        self.row_num = 1

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
        context['new_url'] = 'http://127.0.0.1:8000/admin/course/course/'
        context['cols'] = ["课程名称", "教课老师", "年级", "学生名单", "课时"]
        datas = []
        row_num = 1
        for course in courses:
            logger.error("course: %s" % course)
            teachers = course.teachers.all()
            logger.error("teachers: %s" % teachers)
            for teacher in teachers:
                logger.error("teacher: %s" % teacher)
                row = Row()
                row.row_url = course.get_absolute_url()
                row.pk = course.pk
                row.row_num = row_num
                row_num += 1
                elem = Element()
                elem.elem_url = course.get_absolute_url()
                elem.elem_str = course.name
                logger.error("name row: %s, %s" % (elem.elem_str, elem.elem_url))
                row.elems.append(elem)
                logger.error("elems size %d, %s" % (len(row.elems), str(row.elems)))
                elem2 = Element()
                elem2.elem_url = teacher.get_absolute_url()
                elem2.elem_str = teacher.name
                row.elems.append(elem2)
                elem3 = Element()
                elem3.elem_str = str(course.grade)
                row.elems.append(elem3)
                elem4 = Element()
                students = course.students.all()
                if 2 < len(students):
                    elem4.elem_url = course.get_absolute_url()
                    elem4.elem_str = "..."
                else :
                    elem4.elem_str = str([student.name for student in students])[1:-1]
                    logger.error("elem_str: %s" % elem4.elem_str)
                logger.error("students: %s" % elem4.elem_str)
                row.elems.append(elem4)
                elem5 = Element()
                elem5.elem_str = course.classes
                row.elems.append(elem5)
                datas.append(row)
        context['rows'] = datas
        logger.error("datas size %d" % len(datas))
        logger.error("%s, %s" % (datas[0].elems[0].elem_url, datas[0].elems[0].elem_str))
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

class DetailViews(ListView):
    pass