from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Views currently simply render by using each html file as a template

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
