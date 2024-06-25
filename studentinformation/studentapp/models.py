from django.db import models

class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    phnumber=models.CharField(max_length=10)
    college=models.CharField(max_length=20,null=True)