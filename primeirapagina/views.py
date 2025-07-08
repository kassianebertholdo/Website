from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """
    Render the home page.
    """
    return render(request, 'primeirapagina/home.html', )