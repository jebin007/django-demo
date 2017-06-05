from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widgets=forms.PasswordInput)

    class Meta: #information about the corresponding outer class
        model = User
        fields = ['username','email','password']
