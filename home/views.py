from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    Simply return the render of the home page. To visualize this page the login is required
    """
    return render(request, 'home/home.html')
