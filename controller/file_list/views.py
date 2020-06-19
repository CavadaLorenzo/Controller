from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from file_list.postgresDB import PostgresDB


@login_required
def file_list(request):
    """
    Return the render of the page and the list of the 
    file in the system with the information about the server
    which they belong. To visualize this page the login is required.
    """
    db = PostgresDB()
    file_list = db.get_all()
    context = {"file_list": file_list}
    return render(request, 'file_list/file_list.html', context)
