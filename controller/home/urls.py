"""
| path: ' '
| mapped to: views.home
| name: home-page

| path: 'login/'
| mapped to: views.home
| name: home-login
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('login', views.home, name='home-login'),
]
