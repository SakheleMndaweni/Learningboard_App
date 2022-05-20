from django.db import models

# Create your models here.

class Parent(models.Model):
      name = models.CharField(max_length= 225)
      surname = models.CharField(max_length= 225)
      phone = models.CharField(max_length= 10)
      email = models.EmailField(unique=True)
      id_number = models.CharField(unique=True,max_length= 13)
      image = models.ImageField(upload_to='parent',null=True)
      

class BR_Parents_Students(models.Model):
      parent_id_number  = models.CharField(max_length= 13)
      student_id_number = models.CharField(max_length= 13)

class Meeting(models.Model):
      start = models.DateTimeField()
      end = models.DateTimeField()
      topic = models.CharField(max_length= 225)
      description = models.TextField()
      creator_id = models.CharField(max_length= 13)
      res_id = models.CharField(max_length= 13)


class Validate(models.Model):
      status = models.CharField(max_length= 225)
      parent_id_number =  models.CharField(max_length= 13)
      student_id_number =  models.CharField(max_length= 13)

class Event(models.Model):
      start = models.DateTimeField()
      end = models.DateTimeField()
      topic = models.CharField(max_length= 225)
      description = models.TextField()
