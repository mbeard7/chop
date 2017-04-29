from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import loader


# Views currently simply render by using each html file as a template
# May need to modify if unable to pass what's needed to the front end

def home(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request, 'index.html', context)

def about(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'about.html', context)

@login_required
def references(request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'reference.html',context)

@login_required
def calculator (request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'calculator.html',context)

@login_required
def curriculum (request):
    if request.user.is_authenticated():
        context = {'authenticated': True}
    else:
        context = {'authenticated': False}
    return render(request,'curriculum.html',context)
