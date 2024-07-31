from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path("register/", views.register, name='register'), # registration function in views
    path("login_check/", views.login, name="login_check"),

    # Student Operations
    path('student/', views.option, name='optionpage'),
    path('addstudent/', views.addStudent, name='addstudentpage'),
    path('viewstudent/', views.viewStudent, name='viewstudentpage'),
    path('addDetail/', views.addDetail, name='addDetail'), # student add function for addstudent.html
]