from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', 'Student'],
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


