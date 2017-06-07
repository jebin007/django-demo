from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta: #information about the corresponding outer class
        model = User
        fields = ['username','email','password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='username', max_length=10)

    class Meta: #information about the corresponding outer class
        model = User
        fields = ['username','password']
