from django.http import HttpResponse
from django.shortcuts import render

def display_login_form(request):
    return render(request, "auth/login.html")

def display_create_acount_form(request):
    return render(request, "auth/register.html")

def display_forgot_password_form(request):
    return render(request, "auth/forgot_password.html")