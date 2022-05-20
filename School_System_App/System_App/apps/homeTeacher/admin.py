from django.contrib import admin
from .models import *

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','surname','phone','email','id_number')

admin.site.register(Teacher,TeacherAdmin)