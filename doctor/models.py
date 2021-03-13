from django.db import models

# Create your models here.

class Patient_History(models.Model):
    P_height = models.FloatField()
    P_wait = models.FloatField()
    P_blood_presher = models.FloatField()
    Symptoms = models.CharField(max_length=100)
    

class Medicine(models.Model):
    Name = models.CharField(max_length=100)
    Unit = models.CharField(max_length=100)
    Pack = models.IntegerField()
    Category = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Tax = models.DecimalField()
    Price = models.FloatField()
    IX_code = models.CharField(max_length=100)


class Advice(models.Model):
    Name = models.CharField(max_length=100)
    CreateDate = models.DateTimeField(auto_now_add=True)
    Update_time = models.DateTimeField(auto_now=True)

