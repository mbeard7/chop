from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def references(request):

    return render(request,'reference.html')