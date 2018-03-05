#/bin/bash python
# -*- coding:utf-8 -*-

from django.db import models
from django.urls import reverse

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=30,unique=True)
    sex = models.CharField(max_length=20)
    age = models.IntegerField()
    grade = models.CharField(max_length = 20)
    parent = models.CharField(max_length = 20)
    parent_phone = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/admin/course/student/" + str(self.pk) + "/change/"


class Teacher(models.Model):
    name = models.CharField(max_length=30,unique=True)
    phone = models.CharField(max_length = 20)
    #organization = models.CharField(max_length=50)
    #city = models.CharField(max_length=30)
    def get_absolute_url(self):
        #return reverse('teacher:detail', kwargs={'pk': self.pk})
        return "/admin/course/teacher/" + str(self.pk) + "/change/"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30,unique=True)
    students = models.ManyToManyField(Student) # 一个课程有多个学生
    '''teachers = models.ManyToManyField(Teacher,
        through="ClassInfo", #通过ClassInfo表记录老师与课程的多对多关系
        through_fields = ("course", "teacher")) #一个课有多个老师可以讲
    '''
    teachers = models.ManyToManyField(Teacher)
    grade = models.CharField(max_length=20, default='0')
    tuition = models.IntegerField()
    #startime = models.CharField(max_length=50)
    classes = models.IntegerField() #总课时，一个课一共分成几节
    def get_absolute_url(self):
        #return reverse('course:detail', kwargs={'pk': self.pk})
        return "/admin/course/course/" + str(self.pk) + "/change/"

    def __str__(self):
        return self.name
        #return "%s, %s, %s" % (self.name, self.teachers.all(), self.grade)

    class Meta:
        #unique_together = ["name", "teachers", "grade"]
        pass

class ClassInfo(models.Model):
    '''记录上课课时信息'''
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    #class_len = models.IntegerField() #本节课课时时长。

    def get_absolute_url(self):
        #return reverse('classinfo:detail', kwargs={'pk': self.pk})
        return "/admin/course/classinfo/" + str(self.pk) + "/change/"

    def __str__(self):
        return "%s, %s, %s, %s" % (self.course, self.teacher, self.start_time, self.end_time)
