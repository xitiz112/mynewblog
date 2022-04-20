
from statistics import mode
from django.db import models
from  django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.urls import reverse








class category(models.Model):
    name= models.CharField(max_length=255)


    def __str__(self):
        return (self.name) 


class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField()
    image= models.ImageField(null=True,blank=True, upload_to = "images/")


    
    def __str__(self):
        return str(self.user) 

    def get_absolute_url(self):
        return reverse('home')

   



class post(models.Model):
    title= models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    Category = models.CharField(max_length=255)
    image= models.ImageField(null=True,blank=True, upload_to = "images/")
    post_date= models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.title + '|' + str(self.author ) 


    def get_absolute_url(self):
        return reverse('article-details', kwargs={'pk': self.pk})



 

    
class comment(models.Model):
    post_name=models.ForeignKey(post,related_name="comments",on_delete=models.CASCADE,)
    user_name=models.CharField(max_length=255)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    def __str__(self):

        return '%s - %s' % (self.post_name.title, self.user_name)


    def get_absolute_url(self):
        return reverse('article-details', kwargs={'pk': self.post_name.pk})

 