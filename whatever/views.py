from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return render(request, 'home.html')

def translate(request):
    return HttpResponse('You are on the translation page')