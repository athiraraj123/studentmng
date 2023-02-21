from django.db import models

# Create your models here.

class Students(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=20)
    student_phone=models.CharField(max_length=100)
    student_email=models.CharField(max_length=100)
    student_address=models.CharField(max_length=100)
    student_place=models.CharField(max_length=100)

# class Students(models.Model):
#     student_id=models.AutoField(primary_key=True)
#     student_name=models.CharField(max_length=20)
#     student_phone=models.CharField(max_length=100)
#     student_email=models.CharField(max_length=100)
#     student_address=models.CharField(max_length=100)
#     student_place=models.CharField(max_length=100)
