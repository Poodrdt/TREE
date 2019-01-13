# from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Position(models.Model):
    name  = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname  = models.CharField(max_length=255)
    position  = models.ForeignKey(Position, on_delete=models.PROTECT)
    salary    = models.IntegerField()
    boss      = models.ForeignKey('self', blank=True, on_delete=models.PROTECT)
    employment_start_date = models.DateField()

    def get_full_name(self):
        return self.firstname + " " + self.lastname

    

