from django import forms
from .models import *

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['uploaded_file']