from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request:HttpRequest):

    context = {'texto': 'Está na home'}
    return render(request, 'home/index.html', context)
