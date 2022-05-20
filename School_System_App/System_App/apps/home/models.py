# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
      name = models.CharField(max_length= 225)
      surname = models.CharField(max_length= 225)
      phone = models.CharField(max_length= 10)
      email = models.EmailField(unique=True)
      id_number = models.CharField(max_length= 13)
      image = models.ImageField(upload_to='student',null=True)
      
class News(models.Model):
      topic = models.CharField(max_length= 225)
      description = models.TextField()
      date = models.DateField()
      Author = models.CharField(max_length= 225)
      image = models.ImageField(upload_to='studentNews',null=True)

class Notification(models.Model):
      topic = models.CharField(max_length= 225)
      description = models.TextField()
      date = models.DateField()
      Author = models.CharField(max_length= 225)
      id_number = models.CharField(max_length=13)

class Events(models.Model):
      topic = models.CharField(max_length= 225)
      description = models.TextField()
      Startdate = models.DateTimeField()
      Enddate =models.DateTimeField()
      Author = models.CharField(max_length= 225)

class Mark(models.Model):
      first = models.IntegerField()
      Second = models.IntegerField()
      third= models.IntegerField()
      fourth = models.IntegerField()
      totalmarks = models.IntegerField()
      id_number = models.CharField(max_length=13)
      subject_code = models.CharField(max_length=13,default='not set')

class Subject(models.Model):
      teacher_id_number = models.CharField(max_length=13)
      name = models.CharField(max_length=225)
      subject_code = models.CharField(max_length=13)
      grade = models.IntegerField()


class BR_Subjects_Students(models.Model):
      subject_code = models.CharField(max_length=13)
      id_number = models.CharField(max_length= 13)

class Classrooms(models.Model):
      teacher_id_number = models.CharField(max_length= 13)
      name = models.CharField(max_length=225) 
      student_id_number = models.CharField(max_length= 13)
      grade = models.IntegerField()

class Homework(models.Model):
      topic       = models.CharField(max_length=225)
      description = models.TextField()
      end_date    = models.DateTimeField()
      start_date  = models.DateTimeField()
      student_id_number   = models.CharField(max_length=13)
      teacher_id_number = models.CharField(max_length=13)
      doc         = models.FileField(upload_to='Assessments',null=True)
      sub_assessment = models.CharField(max_length=13,default='not set')
      assessment_code = models.CharField(max_length=225,default='not set')
      subject_code =  models.CharField(max_length=13,default='not set') 

class HomeworkSubmission(models.Model):
      topic       = models.CharField(max_length=225)
      description = models.TextField()
      deadline  = models.DateTimeField()
      student_id_number   = models.CharField(max_length=13,default='not set')
      assessment_code = models.CharField(max_length=225)
      comment =  models.CharField(max_length=225)  
      marks = models.IntegerField()
      assessment_answer =models.FileField(upload_to='AssessmentsSub',null=True)

      


class Attendance_code(models.Model):
      day               = models.DateTimeField()
      code              = models.CharField(max_length=5)
      teacher_id_number = models.CharField(max_length=13)
      subject_code      = models.CharField(max_length=13,default='not set')
      status            = models.CharField(max_length=225,default='not set') 

class Attendance(models.Model):
      day               = models.DateTimeField()
      subject_code      = models.CharField(max_length=13)
      student_id_number = models.CharField(max_length=13)
      code              = models.CharField(max_length=5)

class Assessments(models.Model):
      topic       = models.CharField(max_length=225)
      description = models.TextField()
      end_date    = models.DateTimeField()
      start_date  = models.DateTimeField()
      teacher_id_number = models.CharField(max_length=13)
      doc         = models.FileField(upload_to='Assessments',null=True)
      sub_assessment = models.CharField(max_length=13,default='not set')
      assessment_code = models.CharField(max_length=225,default='not set')
      subject_code =  models.CharField(max_length=13,default='not set') 

class Submission(models.Model):
      topic       = models.CharField(max_length=225)
      description = models.TextField()
      teacher_id_number = models.CharField(max_length=13)
      deadline  = models.DateTimeField()
      assessment_code = models.CharField(max_length=225)
      comment =  models.CharField(max_length=225)  
      marks = models.IntegerField()
      assessment_answer =models.FileField(upload_to='AssessmentsSub',null=True)









