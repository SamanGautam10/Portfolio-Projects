from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path("register/", views.register, name='register'), # registration function in views
    path('login/', views.login_view, name='login'),
    path("login/successful", views.welcome, name="dashboard"),
    path("login/unsuccessful", views.error, name="error"),

    # Student Operations
    path('student/', views.option, name='optionpage'),
    path('addstudent/', views.addStudent, name='addstudentpage'),
    path('viewstudent/', views.viewStudent, name='viewstudentpage'),
    path('addDetail/', views.addDetail, name='addDetail'), # student add function for addstudent.html
]