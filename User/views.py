from dataclasses import fields
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from mypost .models import profile,category
from  django.contrib.auth.models import User
from User.forms import signupform,profilecreateform,passwordresetform
from .serializers  import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class= signupform
    template_name= "registration/register.html"
    success_url= reverse_lazy("login")


class passwordresetview(PasswordChangeView):
    form_class=passwordresetform
    template_name="registration/passwordreset.html"
    success_url = reverse_lazy("login")
   
class profilecreateview(generic.CreateView):
    
    form_class=profilecreateform
    template_name= "registration/createprofile.html"

    def form_valid(self,form):
        form.instance.user= self.request.user
        return super().form_valid(form)



class profileview(generic.DetailView):
    model=  profile
    template_name= "registration/profile.html"


    #def get_context_data(self, *args, **kwargs):
        #context= super(profileview,self).get_context_data(*args, **kwargs)
        #user_profile= get_object_or_404(profile,id=self.kwargs['pk'])
        #context['user_profile']= user_profile
        #return context

    def get_context_data(self, *args, **kwargs):
        context= super(profileview,self).get_context_data(*args, **kwargs)
        user_profile= get_object_or_404(profile,id=self.kwargs['pk'])
        cat_menu= category.objects.all()
        context= super(profileview,self).get_context_data(*args, **kwargs)
       
        context['user_profile']= user_profile
        context['cat_menu']= cat_menu
        return context


    
  


class profileUpdateView(generic.UpdateView):
    model= profile
    template_name="registration/update_profile.html"
    fields= ['bio',"image"]
    success_url= reverse_lazy("home")



    def get_context_data(self, *args, **kwargs):
        cat_menu= category.objects.all()
        context= super(profileUpdateView,self).get_context_data(*args, **kwargs)
        context['cat_menu']= cat_menu
        return context




class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


  






  