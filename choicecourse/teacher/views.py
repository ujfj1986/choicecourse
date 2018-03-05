from django.shortcuts import render
from django.views.generic import ListView
from course.baseviews import *
from course.models import Teacher, Course, ClassInfo

# Create your views here.
class DetailView(ListView):
    pass

class TeacherIndexView(IndexView):
    model = Teacher
    new_url = '/admin/course/teacher/'
    cols = ['教师姓名', '课程名称', '完成课时']

    @classmethod
    def _get_name_element(cls, teacher, course):
        elem = Element()
        elem.elem_str = teacher.name
        elem.elem_url = teacher.get_absolute_url()
        return elem

    @classmethod
    def _get_course_element(cls, teacher, course):
        elem = Element()
        elem.elem_str = course.name
        elem.elem_url = course.get_absolute_url()
        return elem

    @classmethod
    def _get_impl_classes_element(cls, teacher, course):
        classinfos = ClassInfo.objects.filter(teacher = teacher, course = course)
        '''TODO:此处有bug，需要处理同一学期里面的所上课时，而不是所有课时的和'''
        elem = Element()
        elem.elem_str = str(classinfos.count())
        return elem

    def _get_rows(self):
        teachers = Teacher.objects.all()
        rows = []
        row_num = 1
        _help_dic = {
            self.cols[0]: TeacherIndexView._get_name_element,
            self.cols[1]: TeacherIndexView._get_course_element,
            self.cols[2]: TeacherIndexView._get_impl_classes_element,
        }
        for teacher in teachers:
            courses = teacher.course_set.all()
            for course in courses:
                row = Row()
                row.row_url = teacher.get_absolute_url()
                row.pk = teacher.pk
                row.row_num = row_num
                row_num += 1
                for col in self.cols:
                    elem = _help_dic[col](teacher, course)
                    row.elems.append(elem)
                rows.append(row)
        return rows