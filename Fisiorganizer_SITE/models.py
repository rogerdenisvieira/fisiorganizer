from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    # id_state = models.ForeignKey(State, default='1')
    city = models.CharField(max_length=25)
    phone = models.PositiveIntegerField(blank=True, null=True)
    cellphone = models.PositiveIntegerField(blank=True, null=True)
    CEP = models.PositiveIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=False)
    details = models.TextField(max_length=500, blank=True)

class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    id_instructor = models.ForeignKey(User)
    id_customer = models.ForeignKey(Customer)
    id_exercise = models.ForeignKey(Exercise)
    date = models.DateField
    time = models.TimeField

class User_extra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User)
    attempts = models.PositiveIntegerField(blank=False, null=False, default=0)







