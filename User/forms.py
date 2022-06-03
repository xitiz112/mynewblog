import email
from operator import length_hint
from typing import Text
from django import forms
from django.contrib.auth .forms import UserCreationForm,PasswordChangeForm
from django.forms import EmailField, fields, modelformset_factory, widgets
from django.contrib.auth.models import User
from mypost.models import profile



class signupform(UserCreationForm):
    email= forms.EmailField()
    firstname= forms.CharField(max_length=255, widget= forms.TextInput(attrs={"class":"form-control"}))
    lastname= forms.CharField(max_length=255,widget= forms.TextInput(attrs={"class":"form-control"}))
   
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
       
class passwordresetform(PasswordChangeForm):
    old_password= forms.CharField(max_length=255,  label="Old Password",widget= forms.PasswordInput(attrs={"class":"form-control","placeholder":"your old password"}))
    new_password1= forms.CharField(max_length=255, widget= forms.PasswordInput(attrs={"class":"form-control","placeholder":"your new password1"}))
    new_password2= forms.CharField(max_length=255,widget= forms.PasswordInput(attrs={"class":"form-control","placeholder":"your new password2"}))
   
    class meta:
        model=User
        fields=('old_password','new_password1','new_password2')


