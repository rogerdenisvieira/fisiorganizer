from django.db import models
from django.contrib.auth.models import User

# Models .


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    # id_state = models.ForeignKey(State, default='1')
    name = models.CharField(max_length=150, blank=False, default='')
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=25)
    phone = models.PositiveIntegerField(blank=True, null=True)
    age = models.IntegerField(blank=False)
    details = models.TextField(max_length=500, blank=True)


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    reference = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=False)


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    id_instructor = models.ForeignKey(User)
    id_customer = models.ForeignKey(Customer)
    date = models.DateField()
    time = models.TimeField()


class SessionExercise(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise)
    id_session = models.ForeignKey(Session)
    alias = models.CharField(max_length=150, blank=False)


class UserExtra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User)
    attempts = models.PositiveIntegerField(blank=False, null=False, default=0)
