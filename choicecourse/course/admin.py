from django.contrib import admin
from .models import Course, Student, Teacher, ClassInfo

# Register your models here.
admin.site.register(ClassInfo)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
