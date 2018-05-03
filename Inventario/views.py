from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Aca debe ir el Login')
