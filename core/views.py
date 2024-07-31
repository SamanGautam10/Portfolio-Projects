from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


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


# Student operations
def option(request):
    return render(request, 'core/option.html')

def addDetail(request):
    if request.method == 'POST':
        # extraction of student details from student form
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        gender_set = request.POST.get('gender')
        email_set = request.POST.get('email')
        dob_set = request.POST.get('dob')
        faculty_set = request.POST.get('faculty')
        section_set = request.POST.get('section')

        # creating instance of student and adding in database
        studentDetail = StudentDetails(firstname = first_name, 
                                       lastname = last_name, 
                                       gender = gender_set, 
                                       email = email_set, 
                                       dob = dob_set, 
                                       faculty = faculty_set, 
                                       section = section_set)
        studentDetail.save()
        return render(request, 'core/confirmadd.html')
    
    # In Case of error
    else:
        return HttpResponse("You have encountered error")

def addStudent(request):
    return render(request, 'core/addstudent.html')



def viewStudent(request):
    return render(request, 'core/viewstudent.html')