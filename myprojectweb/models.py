from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    qualification = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
