from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# models for registration page
class UserDetail(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    # password hasing function
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

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