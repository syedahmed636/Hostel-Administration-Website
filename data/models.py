from django.db import models

# Create your models here.

class Datadd(models.Model):
    Name = models.CharField(max_length=100)
    ID = models.CharField(max_length=20,primary_key = True)
    Year = models.IntegerField()
    Dept = models.CharField(max_length=50)
    Mbno = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Gmail = models.CharField(max_length=100)
    Roomalloted = models.CharField(max_length=20)
    AmountPaid= models.IntegerField()
    Academicyear = models.CharField(max_length=20)
    ParentMbno = models.CharField(max_length=20)
    CautionDeposit = models.CharField(max_length=50)

class Datadds(models.Model):
    Name = models.CharField(max_length=100)
    ID = models.IntegerField(primary_key = True)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Mbno = models.CharField(max_length=20)
    Gmail = models.CharField(max_length=100)
    Address = models.CharField(max_length=150)
    Alternate_ContactNum = models.CharField(max_length=20)
    Designation = models.CharField(max_length=40)
    Salary = models.IntegerField()






