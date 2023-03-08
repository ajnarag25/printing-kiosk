from ast import Delete
from multiprocessing import context
from tkinter.messagebox import NO
from tkinter.tix import STATUS
from urllib import request
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse

# import json
# from .models import *
# from .forms import *
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import PasswordChangeView
# from django.urls import reverse_lazy
# from django.core.mail import send_mail
# from django.contrib.auth.hashers import check_password
# from django.core import serializers
# from django.http import JsonResponse
# from django.utils.timezone import datetime

# from datetime import date
# from docx import Document
# from docx2pdf import convert
# # import pythoncom
# import os
# import shutil

# Create your views here.
def index(request):
    return render(request, "index.html")

def home_user(request):
    return render(request, "home_user.html")

def home_admin(request):
    return render(request, "home_admin.html")

def login_admin(request):
    return render(request, "login_admin.html")

def user_print(request):
    return render(request, "user_print.html")

def user_select(request):
    return render(request, "user_select.html")