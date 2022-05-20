from django.db import models

# Create your models here.

class Teacher(models.Model):
      name = models.CharField(max_length= 225)
      surname = models.CharField(max_length= 225)
      phone = models.CharField(max_length= 10)
      email = models.EmailField(unique=True)
      id_number = models.CharField(max_length= 13)
      image = models.ImageField(upload_to='Teacher',null=True)