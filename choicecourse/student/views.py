from django.shortcuts import render
from django.views.generic import ListView
from course.models import *
from course.baseviews import *

# Create your views here.
class DetailView(ListView):
    pass

class StudentIndexView(IndexView):
    model = Student
    new_url = '/admin/course/student/'
    cols = ['姓名', '年级', '教课老师', '家长姓名', '家长电话', '课程信息', '已上课时', '总课时']

    #@classmethod
    def _get_name_element(self, **argv):
        student = argv['student']
        elem = Element()
        elem.elem_str = student.name
        elem.elem_url = student.get_absolute_url()
        return elem

    #@classmethod
    def _get_grade_element(self, **argv):
        student = argv['student']
        elem = Element()
        elem.elem_str = str(student.grade)
        return elem

    #@classmethod
    def _get_teacher_element(self, **argv):
        teacherpk = argv['teacher']['teacher']
        teacher = Teacher.objects.get(pk=teacherpk)
        elem = Element()
        elem.elem_str = teacher.name
        elem.elem_url = teacher.get_absolute_url()
        return elem

    #@classmethod
    def _get_parent_element(self, **argv):
        student = argv['student']
        elem = Element()
        elem.elem_str = student.parent
        return elem

    #@classmethod
    def _get_parent_phone_element(self, **argv):
        student = argv['student']
        elem = Element()
        elem.elem_str = student.parent_phone
        return elem

    #@classmethod
    def _get_course_element(self, **argv):
        coursepk = argv['course']['course']
        course = Course.objects.get(pk = coursepk)
        elem = Element()
        elem.elem_str = course.name
        elem.elem_url = course.get_absolute_url()
        return elem

    #@classmethod
    def _get_class_info_element(self, **argv):
        coursepk = argv['course']['course']
        teacherpk = argv['teacher']['teacher']
        classinfos = argv['classinfos']
        num_classes = classinfos.filter(course=coursepk, teacher=teacherpk).count()
        elem = Element()
        elem.elem_str = str(num_classes)
        return elem

    #@classmethod
    def _get_class_count_element(self, **argv):
        coursepk = argv['course']['course']
        course = Course.objects.get(pk = coursepk)
        elem = Element()
        elem.elem_str = str(course.classes)
        return elem

    _handler_dic = {
        cols[0]: _get_name_element,
        cols[1]: _get_grade_element,
        cols[2]: _get_teacher_element,
        cols[3]: _get_parent_element,
        cols[4]: _get_parent_phone_element,
        cols[5]: _get_course_element,
        cols[6]: _get_class_info_element,
        cols[7]: _get_class_count_element,
    }
    def _get_rows(self):
        students = Student.objects.all()
        rows = []
        row_num = 1
        for student in students:
            #TODO:根据学生所上的课程信息，查询学生所报的课程和老师
            #还需要根据时间进行过滤。
            classinfos = student.classinfo_set
            courses = classinfos.values('course').distinct()
            logger.error("courses: %s" % courses)
            for course in courses:
                teachers = classinfos.filter(course = course['course']).values('teacher').distinct()
                for teacher in teachers:
                    row = Row()
                    row.row_num = row_num
                    row_num += 1
                    row.row_url = student.get_absolute_url()
                    row.pk = student.pk
                    for col in self.cols:
                        elem = self._handler_dic[col](self,
                            student=student,
                            course=course,
                            teacher=teacher, 
                            classinfos = classinfos)
                        row.elems.append(elem)
                    rows.append(row)
        return rows


