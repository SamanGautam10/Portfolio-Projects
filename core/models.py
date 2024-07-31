from django.db import models

# models for registration page
class UserDetail(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.userId} - {self.username}"
    
class StudentDetails(models.Model):
    studentId = models.AutoField(primary_key=True)
    firstname =  models.TextField(max_length=40)
    lastname = models.TextField(max_length=40)
    gender = models.CharField(max_length=20)
    email = models.EmailField(max_length=80)
    dob = models.DateField()
    faculty = models.CharField(max_length=80)
    section = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.section} - {self.studentId}"