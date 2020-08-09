from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
User=get_user_model()

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=150,widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=128)
    phone=forms.CharField(max_length=30)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput())

    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('This username is taken')
        return self.cleaned_data['username']

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password donot match')

