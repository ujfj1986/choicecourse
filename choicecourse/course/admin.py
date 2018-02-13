from django.contrib import admin
from .models import Course, Students, Teacher, ClassInfo

# Register your models here.
admin.site.register(ClassInfo)
admin.site.register(Course)
admin.site.register(Students)
admin.site.register(Teacher)
