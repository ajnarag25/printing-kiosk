from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import requests
import json
import os
import subprocess
from django.contrib import messages
#fsdlkfjsdlkfajsdklf
# import json
# from .models import *
# from .forms import *
# from django.contrib.auth import authenticate, login, logout
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

def loader(request):
    return render(request, "loader.html")


def user_select(request):
    if request.method == 'POST':
        filename = request.FILES['uploaded_file']
        name_file = os.path.splitext(str(filename))[0]
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            directory_path = 'uploads/'
            files = os.listdir(directory_path)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)))
            latest_file = files[-1]
            instructions = {
                'parts': [
                    {
                    'file': 'document'
                    }
                ]
            }
            response = requests.request(
                'POST',
                'https://api.pspdfkit.com/build',
                headers = {
                    'Authorization': 'Bearer pdf_live_fks3MaKwGQAaRm6H1atpHAGJalfmNAXLqorSmjhf6HX'
                },
                files = {
                    'document': open('uploads/'+str(latest_file), 'rb')
                },
                data = {
                    'instructions': json.dumps(instructions)
                },
                stream = True
            )

            if response.ok:
                with open('converted_files/'+str(name_file)+'.pdf', 'wb') as fd:
                    for chunk in response.iter_content(chunk_size=8096):
                        fd.write(chunk)
                    return redirect ('loader')
                    # else:
                    #     print(response.text)
                    #     exit()
            else:
                messages.info(request,'Error uploading file')
                print('error uploading file')
        else:
            messages.info(request,'Error uploading file')
            print('error uploading file')
    else:
        form = UploadFileForm()
    return render(request, 'user_select.html', {'form': form})




