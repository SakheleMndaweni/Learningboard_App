# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
      list_display = ('name','teacher_id_number','subject_code','grade')

admin.site.register(Subject,SubjectAdmin)

#remeve after testing
admin.site.register(BR_Subjects_Students)
admin.site.register(Mark)

class StudentAdmin(admin.ModelAdmin):
      list_display = ('name','surname','phone','id_number','email','image')

admin.site.register(Student,StudentAdmin)