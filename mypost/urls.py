from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from . import views
from .views import ArticleUpdateView, commentview, createpostview, homeview , detailview ,categoryview,ArticleDeleteView,authorview, searchview
urlpatterns = [
    path('', homeview.as_view(), name='home'),
    path('article/<int:pk>',detailview.as_view(), name='article-details'),
    path("create/",createpostview.as_view(),name='article-create'),
    path("article/<int:pk>/comment" ,commentview.as_view(),name='article-comment'),
    path("category/<str:cats>",categoryview, name="category"),
    path("<int:pk>/author",authorview, name="author"),
    path("article/edit/<int:pk>",ArticleUpdateView.as_view(),name='article-update'),
    path("article/delete/<int:pk>",ArticleDeleteView.as_view(),name='article-delete'),
    path("search",searchview,name='search'),
  


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

