from django import forms
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=100, )
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('User Exists')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('email already exist')
        return email


class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'first_name', 'last_name', 'country', 'city', 'address', 'image', 'telegram_id',)
