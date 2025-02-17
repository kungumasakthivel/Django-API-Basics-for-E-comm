from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader

def say_hello(request):
    return HttpResponse('Hello World')

def say_hello(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())