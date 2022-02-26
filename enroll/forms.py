from django.core import validators
from django import forms
from .models import SudentModel


class Sudent_data(forms.ModelForm):
   class Meta:
     model=SudentModel
     fields='__all__'
     label={'email':'Email'}
     widgets={
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.EmailInput(attrs={'class':'form-control'}),
         'password': forms.PasswordInput(render_value=True , attrs ={'class':'form-control' }),

     }