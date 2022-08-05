from django.db import models
# Create your models here.

class Patient(models.Model):
    fullname= models.CharField(max_length=100)
    pat_code= models.CharField(max_length=20)
    birthday= models.CharField(max_length=30)
    mobile= models.CharField(max_length=15)

class Prescription(models.Model):
    fullname= models.CharField(max_length=100)
    pat_code= models.CharField(max_length=20)
    mobile= models.CharField(max_length=15)
    prescription= models.CharField(max_length=1000)
    date = models.DateField(max_length=30 )


