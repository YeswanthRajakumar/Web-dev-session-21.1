
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.getPostsList,name="post-list"),
    path('home/', views.getHome,name="home"),
    
    
]