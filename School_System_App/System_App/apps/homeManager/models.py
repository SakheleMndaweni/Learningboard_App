from django.db import models

# Create your models here.

class SchoolManager(models.Model):
      name = models.CharField(max_length= 225)
      surname = models.CharField(max_length= 225)
      phone = models.CharField(max_length= 10)
      email = models.EmailField(unique=True)
      id_number = models.CharField(max_length= 13)
      image = models.ImageField(upload_to='SchoolManager',null=True,default="media/student/Desktop_-_1.png")