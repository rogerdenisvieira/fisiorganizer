from django.db import models
from django.contrib.auth.models import User
from Fisiorganizer_SITE.validators import validate_phone


# Models .

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    # id_state = models.ForeignKey(State, default='1')
    name = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=25)
    cellphone = models.PositiveIntegerField(blank=False, null=False)
    details = models.TextField(max_length=500, blank=True)
    born_date = models.DateField(blank=False, default='1900-01-01')

    def __str__(self):
        return self.name


class Modality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return str(self.id) + ' - ' + self.name   

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.name

    
class Session(models.Model):
    id = models.AutoField(primary_key=True)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

class UserExtra(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attempts = models.PositiveIntegerField(blank=False, null=False, default=0)

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    city = models.CharField(max_length=25, blank=False)
    phone = models.CharField(blank=False, null=False,max_length=13, validators=[validate_phone])
    details = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.name

class Evolution(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description_before = models.TextField(max_length=500, blank=False)
    description_after = models.TextField(max_length=500, blank=False)

    


