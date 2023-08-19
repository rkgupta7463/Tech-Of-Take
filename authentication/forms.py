from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User 
from django import forms
from django.contrib.auth.forms import PasswordResetForm

class ForgetPass(SetPasswordForm):
    new_password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label='Password Confirm', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    fields=['username','new_password1','new_password2']

    class Meta:
        model=SetPasswordForm
        fields=['username','new_password1','new_password2']