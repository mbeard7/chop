from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request,'template.html')

def about(request):

    return render(request,'about.html')

def references(request):

    return render(request,'reference.html')

def calculator (request):

    return render(request,'calculator.html')

def curriculum (request):

    return render(request,'curriculum.html')