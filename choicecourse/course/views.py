# /bin/bash python
# -*- coding: utf-8 -*-
# author: Jinjing Shan

from django.shortcuts import render
from django.views.generic import ListView
from .models import Student, Course
from .baseviews import IndexView, Element, Row

import logging

logger = logging.getLogger('course.view')

# Create your views here.
class CourseIndexView(IndexView):
    model = Course
    new_url = 'http://127.0.0.1:8000/admin/course/course/'
    cols = ["课程名称", "教课老师", "年级", "学生名单", "总课时"]

    @staticmethod
    def _get_name_element(course):
        elem = Element()
        elem.elem_url = course.get_absolute_url()
        elem.elem_str = course.name
        logger.error("name row: %s, %s" % (elem.elem_str, elem.elem_url))
        return elem

    @staticmethod
    def _get_teacher_element(teacher):
        elem = Element()
        elem.elem_url = teacher.get_absolute_url()
        elem.elem_str = teacher.name
        return elem

    @staticmethod
    def _get_grade_element(course):
        elem = Element()
        elem.elem_str = str(course.grade)
        return elem

    @staticmethod
    def _get_students_element(course):
        elem = Element()
        students = course.students.all()
        if 2 < len(students):
            elem.elem_url = course.get_absolute_url()
            elem.elem_str = "..."
        else :
            elem.elem_str = str([student.name for student in students])[1:-1]
        logger.error("students: %s" % elem.elem_str)
        return elem

    @staticmethod
    def _get_classes_element(course):
        elem = Element()
        elem.elem_str = course.classes
        return elem

    def _get_rows(self):
        courses = Course.objects.all()
        rows = []
        row_num = 1
        _help_dic = {
            self.cols[0]: CourseIndexView._get_name_element,
            self.cols[1]: CourseIndexView._get_teacher_element,
            self.cols[2]: CourseIndexView._get_grade_element,
            self.cols[3]: CourseIndexView._get_students_element,
            self.cols[4]: CourseIndexView._get_classes_element,
        }
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
                for col in self.cols:
                    elem = _help_dic[col](course) if not col == '教课老师' else _help_dic[col](teacher)
                    row.elems.append(elem)
                rows.append(row)
        logger.error("datas size %d" % len(rows))
        logger.error("%s, %s" % (rows[0].elems[0].elem_url, rows[0].elems[0].elem_str))
        return rows

class DetailViews(ListView):
    pass