from django.shortcuts import render
from django.views.generic import ListView
from course.models import ClassInfo
from course.baseviews import *
from django.utils.timezone import localtime

# Create your views here.
class DetailView(ListView):
    pass

class ClassInfoIndexView(IndexView):
    model = ClassInfo
    cols = ['开始时间', '结束时间', '课程名称', '老师', '学生']
    new_url = '/admin/course/classinfo/'

    def _get_start_time_element(self, classinfo):
        elem = Element()
        elem.elem_str = localtime(classinfo.start_time).strftime("%y-%m-%d %X")
        return elem

    def _get_end_time_element(self, classinfo):
        elem = Element()
        elem.elem_str = localtime(classinfo.end_time).strftime("%y-%m-%d %X")
        return elem

    def _get_course_element(self, classinfo):
        elem = Element()
        #course = Course.objects.get(pk = classinfo.values('course']))
        course = classinfo.course
        elem.elem_str = course.name
        elem.elem_url = course.get_absolute_url()
        return elem

    def _get_teacher_element(self, classinfo):
        elem = Element()
        #teacher = Teacher.objects.get(pk = classinfo.values('teacher'))
        teacher = classinfo.teacher
        elem.elem_str = teacher.name
        elem.elem_url = teacher.get_absolute_url()
        return elem

    def _get_students_element(self, classinfo):
        students = classinfo.students.all()
        elem = Element()
        if 2 < len(students):
            elem.elem_str = '...'
            elem.elem_url = classinfo.get_absolute_url()
        else :
            elem.elem_str = str([student.name for student in students])[1:-1]
        return elem

    _handler_dic = {
        cols[0]: _get_start_time_element,
        cols[1]: _get_end_time_element,
        cols[2]: _get_course_element,
        cols[3]: _get_teacher_element,
        cols[4]: _get_students_element,
    }

    def _get_rows(self):
        classinfos = ClassInfo.objects.all()
        rows = []
        row_num = 1

        for classinfo in classinfos:
            row = Row()
            row.row_url = classinfo.get_absolute_url()
            row.pk = classinfo.pk
            row.row_num = row_num
            row_num += 1
            for col in self.cols:
                elem = self._handler_dic[col](self, classinfo)
                row.elems.append(elem)
            rows.append(row)
        return rows

    