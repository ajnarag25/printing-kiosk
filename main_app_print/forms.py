from django import forms
from .models import *
from django.contrib.auth.forms import PasswordChangeForm


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['uploaded_file', 'is_converted']


class price(forms.ModelForm):
    class Meta:
        model = admin_price
        fields = '__all__'


class timer(forms.ModelForm):
    class Meta:
        model = admin_timer
        fields = '__all__'


class CustomPasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))

    def save(self, user):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password1')
        if not user.check_password(old_password):
            raise forms.ValidationError(
                "Your old password was entered incorrectly. Please enter it again.")
        user.set_password(new_password)
        user.save()
        return user
