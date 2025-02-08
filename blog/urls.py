from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add/', views.add_post, name='add-post'),
    
]
