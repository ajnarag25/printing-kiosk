from django import forms
from .models import *


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['uploaded_file','is_converted']


class price(forms.ModelForm):
    class Meta:
        model = admin_price
        fields = '__all__'


class password(forms.ModelForm):
    class Meta:
        model = admin_password
        fields = '__all__'


class timer(forms.ModelForm):
    class Meta:
        model = admin_timer
        fields = '__all__'
