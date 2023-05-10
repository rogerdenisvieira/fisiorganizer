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
    id_level = models.ForeignKey(Level, on_delete=models.CASCADE)
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
    id_modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    id_instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    
class SessionExercise(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    id_session = models.ForeignKey(Session, on_delete=models.CASCADE)
    alias = models.CharField(max_length=150, blank=False)


class UserExtra(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    id_focus = models.ForeignKey(Focus, on_delete=models.CASCADE)


class ExerciseEquipment(models.Model):
    id = models.AutoField(primary_key=True)
    id_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)


    



