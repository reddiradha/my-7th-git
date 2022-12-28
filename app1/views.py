from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def str1(request):
    return HttpResponse('this is first view in app1')
def str2(request):
    return HttpResponse('<h1>this is second view in app1</h1>')
