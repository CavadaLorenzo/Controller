"""copycat URL Configuration

| path: 'admin'
| mapped to: admin.site.urls
| name: admin
 
| path: 'copycat'
| mapped to: include('copycat.urls')

| path: ' '
| mapped to: include('home.urls')

| path: 'login/'
| mapped to: auth_views.LoginView.as_view(template_name='home/login.html')
| name: login

| path: 'logout/'
| mapped to: auth_views.LogoutView.as_view(template_name='home/logout.html')
| name: logout

| path: 'filelist'
| mapped to: include('file_list.urls')
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('copycat/', include('copycat.urls')),
    path('filelist/', include('file_list.urls')),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/logout.html'), name='logout'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)