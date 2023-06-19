from django.contrib import admin
from django.urls import path
from . import views
from .views import home #contact_view

urlpatterns = [
    path('index/',views.home,name='index.html'),
    # path('contact/', views.contact_view, name='contact_view'),
    
]