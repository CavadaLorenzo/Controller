"""copycat URL Configuration

| path: ' '
| mapped to: views.copycat
| name: copycat
 
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.copycat, name='copycat'),
]
