from pyexpat import model
from tkinter import Widget
from django import forms
from .models import User


#To create form using form api.
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name' , 'email' , 'password']
        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'password': forms.PasswordInput(attrs = {'class': 'form-control'}),
        }