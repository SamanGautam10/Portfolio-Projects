from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetail


def index(request):
    return render(request, 'core/index.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        gender_select = request.POST.get('gender')
        email_address = request.POST.get('email')
        password_set = request.POST.get('password')

        # Create a new user entry in the database using the UserDetail model
        userDetail = UserDetail(username = user_name, gender = gender_select, email = email_address, password = password_set)
        userDetail.save()

        return render(request, 'core/confirm.html')
    
    else:
        return HttpResponse("Error Happen")
    

def login(request):
    return render(request, 'core/login.html')