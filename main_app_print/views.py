from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
import requests
import json
import os
import subprocess
from django.contrib import messages
import socket
import win32print
import win32api
import subprocess
from pdf2docx import parse
from docx2pdf import convert
GHOSTSCRIPT_PATH = "C:\\Users\\admin\\Desktop\\gs\\bin\\gswin32.exe"
GSPRINT_PATH = "C:\\Users\\admin\\Desktop\\gs\\gsprint.exe"

# fsdlkfjsdlkfajsdklf
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
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    if request.method == 'POST':
        filename = request.FILES['uploaded_file']
        name_file = os.path.splitext(str(filename))[0]
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            directory_path = 'uploads/'
            files = os.listdir(directory_path)
            files.sort(key=lambda x: os.path.getmtime(
                os.path.join(directory_path, x)))
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
                headers={
                    'Authorization': 'Bearer pdf_live_fks3MaKwGQAaRm6H1atpHAGJalfmNAXLqorSmjhf6HX'
                },
                files={
                    'document': open('uploads/'+str(latest_file), 'rb')
                },
                data={
                    'instructions': json.dumps(instructions)
                },
                stream=True
            )

            if response.ok:
                with open('converted_files/'+str(name_file)+'.pdf', 'wb') as fd:
                    for chunk in response.iter_content(chunk_size=8096):
                        fd.write(chunk)
                    return redirect('loader')
                    # else:
                    #     print(response.text)
                    #     exit()
            else:
                messages.info(request, 'Error uploading file')
                print('error uploading file')
        else:
            messages.info(request, 'Error uploading file')
            print('error uploading file')
    else:
        form = UploadFileForm()
    return render(request, 'user_select.html', {'form': form, 'ipadd': IPAddr})

def print_option(request):
    if request.method == 'POST':
        pdf_path = "C:/Users/admin/Downloads/General-features.pdf"
        docx_path = "docx_mod.docx"
        parse(pdf_path, docx_path)
        #back to pdf and then preview
        convert("docx_mod.docx","C:/xampp/htdocs/print_kiosk_main/printing-kiosk/main_app_print/static/pdf_file/to_be_print.pdf")

        
        printer_name = request.POST.get('printer_name')
        copies = request.POST.get('copies')
        size = request.POST.get('size')
        orientation = request.POST.get('orientation')
        rangee = request.POST.get('rangee') 
        
        return redirect("loader_convert_docx")
        
        # currentprinter = win32print.GetDefaultPrinter()
        # currentprinter = printer_name
        # rangee_obj = "-"+str(rangee)
        # orientation = "-" + str(orientation)

        # params = '-ghostscript "'+ GHOSTSCRIPT_PATH  +'" -printer "'+currentprinter+'" -all -portrait -copies 1 "C:\\xampp\\htdocs\\printing_kiosk\\printing_kiosk\\main_app_print\\COLORED_PAGE.pdf"'

        # win32api.ShellExecute(0, 'open', GSPRINT_PATH, params, '.',0)
    return render(request,'printing_options.html')

def print_preview(request):
    return render(request,'print_preview.html')

def print_pay(request):
    return render(request,'pay.html')

def loader_convert_docx(request):
    return render(request,'loader_convert_docx.html')