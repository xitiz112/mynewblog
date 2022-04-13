import email
from operator import length_hint
from typing import Text
from django import forms
from django.contrib.auth .forms import UserCreationForm
from django.forms import EmailField, fields, modelformset_factory, widgets
from django.contrib.auth.models import User
from mypost.models import profile



class signupform(UserCreationForm):
    email= forms.EmailField()
    firstname= forms.CharField(max_length=255, widget= forms.TextInput(attrs={"class":"form-control"}))
    lastname= forms.CharField(max_length=255)
   
    class meta:
        model=User
        fields=('username','firstname','lastname','email','password1','password2')


class profilecreateform(forms.ModelForm):

    class Meta:
      
        model= profile
        fields={'bio','image'}
     
        widgets={
           
        'bio': forms.Textarea(attrs={"class":"form-control","placeholder":"your bio"}),
                
        
       }


