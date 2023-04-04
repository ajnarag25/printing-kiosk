from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
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
import docx
from docx.enum.section import WD_ORIENT
# fsdlkfjsdlkfajsdklf
import json
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.core import serializers
from django.http import JsonResponse
from django.utils.timezone import datetime

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


@login_required(login_url='login_admin')
def home_admin(request):
    view_prices = admin_price.objects.filter(id=1).values()
    view_timer = admin_timer.objects.values()
    get_black = request.POST.get('black')
    get_colored = request.POST.get('colored')
    get_timer = request.POST.get('time')
    if request.method == 'POST' and get_black != None and get_colored != None:
        if admin_price.objects.filter(black=get_black, colored=get_colored).exists():
            messages.info(request, 'No Changes Detected')
        elif int(get_black) <= 0 or int(get_colored) <= 0:
            messages.info(
                request, 'Please do not set a value equal to 0 or below')
        else:
            admin_price.objects.filter(id=1).update(
                black=get_black, colored=get_colored)
            messages.info(request, 'Successfully Update the Price')
            return redirect('home_admin')

    if request.method == 'POST' and get_timer != None:
        if admin_timer.objects.filter(time=get_timer).exists():
            messages.info(request, 'No Changes Detected')
        elif int(get_timer) <= 0:
            messages.info(
                request, 'Please do not set a value equal to 0 or below')
        else:
            admin_timer.objects.filter(id=1).update(
                time=get_timer)
            messages.info(request, 'Successfully Update the Timer')
            return redirect('home_admin')

    context = {
        'prices': view_prices,
        'timer': view_timer
    }

    return render(request, "home_admin.html", context)


def login_admin(request):
    if request.user.is_authenticated:
        return redirect('home_admin')
    elif request.POST.get('admin_password') == '':
        messages.info(request, 'Please Enter your Password!')
    else:
        if request.method == 'POST':
            passw = request.POST.get('admin_password')
            user = authenticate(request, username='admin', password=passw)

            if user is not None:
                login(request, user)
                return redirect('home_admin')

            else:
                messages.info(request, 'Password is Incorrect!')

    return render(request, "login_admin.html")


def user_print(request):
    return render(request, "user_print.html")


def loader(request):
    return render(request, "loader.html")

def mobile_upload(request):
    return render(request, "mobile_upload.html")


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
        # pdf_path = "C:/Users/admin/Downloads/General-features.pdf"
        pdf_path = "C:/Users/admin/Downloads/COLORED_PAGE.pdf"
        docx_path = "docx_mod.docx"
        parse(pdf_path, docx_path)
        # back to pdf and then preview

        printer_name = request.POST.get('printer_name')
        copies = request.POST.get('copies')
        size = request.POST.get('size')
        color_mode = request.POST.get('color_mode')
        orientationn = request.POST.get('orientation')
        rangee = request.POST.get('rangee')
        custom_range = request.POST.get('custom_range')

        official_range = ""
        if rangee == "custom":
            official_range = custom_range
        else:
            official_range = rangee

        doc = docx.Document(docx_path)
        section_size = doc.sections[0]
        sections_orientation = doc.sections

        # for customizing the paper sizes
        if size == "letter":
            section_size.page_width = docx.shared.Inches(8.5)
            section_size.page_height = docx.shared.Inches(11)
        elif size == "a4":
            section_size.page_width = docx.shared.Inches(8.27)
            section_size.page_height = docx.shared.Inches(11.69)
        elif size == "executive":
            section_size.page_width = docx.shared.Inches(7.25)
            section_size.page_height = docx.shared.Inches(10.5)
        elif size == "legal":
            section_size.page_width = docx.shared.Inches(8.5)
            section_size.page_height = docx.shared.Inches(14)
        
        for section in sections_orientation:
            if orientationn == "landscape":
                if section.orientation == WD_ORIENT.PORTRAIT:
                    section.orientation = WD_ORIENT.LANDSCAPE
                    new_width, new_height = section.page_height, section.page_width
                    section.page_width = new_width
                    section.page_height = new_height
                else:
                    pass
            elif orientationn == "portrait":
                if section.orientation == WD_ORIENT.LANDSCAPE:
                    section.orientation = WD_ORIENT.PORTRAIT
                    new_width, new_height = section.page_height, section.page_width
                    section.page_width = new_width
                    section.page_height = new_height
                else:
                    pass

        doc.save(docx_path)
        convert(docx_path, "C:/xampp/htdocs/print_kiosk_main/printing-kiosk/main_app_print/static/pdf_file/to_be_print.pdf")
        return redirect("loader_convert_docx")
        # currentprinter = win32print.GetDefaultPrinter()
        # currentprinter = printer_name
        # rangee_obj = "-"+str(rangee)
        # orientation = "-" + str(orientation)

        # params = '-ghostscript "'+ GHOSTSCRIPT_PATH  +'" -printer "'+currentprinter+'" -all -portrait -copies 1 "C:\\xampp\\htdocs\\printing_kiosk\\printing_kiosk\\main_app_print\\COLORED_PAGE.pdf"'

        # win32api.ShellExecute(0, 'open', GSPRINT_PATH, params, '.',0)
    return render(request, 'printing_options.html')


def print_preview(request, color_mode):
    context = {'color_mode': color_mode}
    return render(request, 'print_preview.html', context)


def print_pay(request):
    return render(request, 'pay.html')


def loader_convert_docx(request):
    return render(request, 'loader_convert_docx.html')


def logout_admin(request):
    logout(request)
    return redirect('login_admin')
