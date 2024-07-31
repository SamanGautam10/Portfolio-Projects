from django.contrib import admin
from .models import * #importing UserDetail from models

# Register your models here.

admin.site.register(UserDetail) # registering userdetail in admin
admin.site.register(StudentDetails)
