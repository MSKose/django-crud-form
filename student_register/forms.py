from tkinter.ttk import Widget
from django import forms
from django.forms import fields
from .models import Student

class PersonForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname','number','mobile', 'email', 'gender','path')

        '''
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full naaaame'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'path': forms.Select(attrs={'class': 'form-control'}),
        }
        '''