from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Views currently simply render by using each html file as a template
# May need to modify if unable to pass what's needed to the front end

def home(request):

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def references(request):

    return render(request,'reference.html')

def calculator (request):

    return render(request,'calculator.html')

def curriculum (request):

    return render(request,'curriculum.html')