from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse('Página de cadastro')

def login(request):
    return HttpResponse('Página de login')

def home(request):
    return HttpResponse('hello world')
