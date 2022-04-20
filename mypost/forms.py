

from django import forms
from .models import category, comment, post
from django.utils.translation import gettext_lazy as _


Choices = category.objects.all().values_list("name","name")


choicelist= []
for item in Choices:
    choicelist.append(item)






class Postform(forms.ModelForm):

    class Meta:
      
        model= post
        fields=("title",'author',"content","Category","image")
     
        widgets={
           
             "Category": forms.Select(choices= Choices, attrs={"class":"form-control"}) ,
                
        
       }

class commentform(forms.ModelForm):

    class Meta:
      
        model= comment
        fields=("user_name","body")
     
        widgets={
           
        "user_name": forms.TextInput( attrs={"class":"form-control","placeholder":"your name"}),
        "body": forms.Textarea(attrs={"class":"form-control","placeholder":"your comment"}),
                
        
       }
     
      



