from turtle import position
from django.db import models

# Create your models here.
# class Position(models.Model):
    # title = models.CharField(max_length=50)
class Employee(models.Model):
    fullname = models.CharField(max_length=20)
    empcode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=11)
    position = models.CharField(max_length=1000)

    def __str__(self):
        return self.fullname
