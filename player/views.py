from django.shortcuts import render

# Create your views here.


def base(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html')
