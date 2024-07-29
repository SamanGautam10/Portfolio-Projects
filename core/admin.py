from django.contrib import admin
from .models import UserDetail #importing UserDetail from models

# Register your models here.

admin.site.register(UserDetail) # registering userdetail in admin
