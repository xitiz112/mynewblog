from unicodedata import name
from xml.etree.ElementInclude import include
from django import urls
from django.urls import include , path
from .views import UserRegisterView, profileview, profileUpdateView,profilecreateview,passwordresetview
from rest_framework import routers
from .import views




router = routers.DefaultRouter()
router.register(r'user', views.userViewSet)

urlpatterns = [
   
    path("registerdeny/",UserRegisterView.as_view(),name='register'), 
    path("create-profile/",profilecreateview.as_view(),name='create-profile'),
    path("<int:pk>/profile",profileview.as_view(),name='profile'), 
    path("profile/edit/<int:pk>",profileUpdateView.as_view(),name='profile-update'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path("password",passwordresetview.as_view(),name='password_reset'),
    
    ]
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.