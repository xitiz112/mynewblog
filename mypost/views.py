
from multiprocessing import context
from urllib import request
from django.forms import SlugField
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import category,post,profile,comment
from .forms import Postform, commentform





class homeview(ListView):
    model= post
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu= category.objects.all()
        cat_post0= post.objects.filter(Category="sports")[:3]
        cat_post1= post.objects.filter(Category="politics")
        context= super(homeview,self).get_context_data(*args, **kwargs)
        context['cat_post0']= cat_post0
        context['cat_post1']= cat_post1
        context['cat_menu']= cat_menu
        return context
    
   

   







    

   
class detailview(DetailView):
    model=post
    template_name="detail.html"
    


    def get_context_data(self, **kwargs):
        #Post=post.objects.get(pk=pk)
        #comments=comment.objects.filter(Post=Post).count()
        cat_menu= category.objects.all()
        context= super(detailview,self).get_context_data(**kwargs)
        context["cat_menu"]=cat_menu
        #context['comments']=comments
        return context

    

 

    

class commentview(CreateView):
    model= comment
    form_class=commentform
    template_name="comment.html"
    
  

    def form_valid(self,form):
        form.instance.post_name_id=self.kwargs['pk']
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        cat_menu= category.objects.all()
        context= super(commentview,self).get_context_data(**kwargs)
        context["cat_menu"]=cat_menu
        return context





class createpostview(CreateView):
    model= post
    form_class= Postform
    template_name="create.html" 



    
    
   
   

    def get_context_data(self, *args, **kwargs):
            cat_menu= category.objects.all()
            context= super(createpostview,self).get_context_data(*args, **kwargs)
            context['cat_menu']= cat_menu
            return context





 
def categoryview(request,cats):
    category_post= post.objects.filter(Category= cats)
    cat_menu= category.objects.all()
    return render(request,"category.html",{"cats":cats,"category_post": category_post, 'cat_menu':cat_menu})






def authorview(request,pk ):
    user_post = post.objects.filter(author=pk)
    user_name= profile.objects.filter(user=pk)
    cat_menu= category.objects.all()
    return render(request,"author.html",{"user_post": user_post,'cat_menu':cat_menu,"user_name": user_name})

  






class ArticleUpdateView(UpdateView):
    model= post
    template_name="update.html"
    fields= ["title",'author',"content","image"]


    def get_context_data(self, *args, **kwargs):
        cat_menu= category.objects.all()
        context= super(ArticleUpdateView,self).get_context_data(*args, **kwargs)
        context['cat_menu']= cat_menu
        return context




class ArticleDeleteView(DeleteView): 
    model=post
    template_name="delete.html"
    success_url= reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        cat_menu= category.objects.all()
        context= super(ArticleDeleteView,self).get_context_data(*args, **kwargs)
        context['cat_menu']= cat_menu
        return context







     







    











