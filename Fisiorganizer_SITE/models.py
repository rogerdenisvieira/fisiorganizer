from django.db import models
from django.contrib.auth.models import User


# Models .

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    # id_state = models.ForeignKey(State, default='1')
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=25)
    cellphone = models.PositiveIntegerField(blank=False, null=False)
    age = models.IntegerField(blank=False)
    details = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Modality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    id_level = models.ForeignKey(Level)
    name = models.CharField(max_length=150, blank=False)
    reference = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name
    
    
class Session(models.Model):
    id = models.AutoField(primary_key=True)
    id_modality = models.ForeignKey(Modality)
    id_instructor = models.ForeignKey(User)
    id_customer = models.ForeignKey(Customer)
    date = models.DateField()
    time = models.TimeField()

    
class SessionExercise(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise)
    id_session = models.ForeignKey(Session)


class UserExtra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User)
    attempts = models.PositiveIntegerField(blank=False, null=False, default=0)


class Focus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class ExerciseFocus(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise)
    id_focus = models.ForeignKey(Focus)


class ExerciseEquipment(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise)
    id_equipment = models.ForeignKey(Equipment)


    



