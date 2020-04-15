from django.urls import path
from . import views

urlpatterns = [
    path('', views.copycat, name='copycat'),
    path('result/', views.result, name='result'),
]
