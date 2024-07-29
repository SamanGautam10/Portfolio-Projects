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