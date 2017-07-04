from django.db import models

# Create your models here.

class person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    age = models.IntegerField(blank=False)
    details = models.TextField(max_length=500, blank=True)
    role = models.IntegerField(blank=False)


class exercise(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

class role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

class session:
    id = models.AutoField(primary_key=True)
    id_instructor = models.ForeignKey(person)
    id_customer = models.ForeignKey(person)
    date = models.DateField
    time = models.TimeField




