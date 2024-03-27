from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html', context={'summary': 1000})
    # return render(request, 'test.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def forgot_password(request):
    return render(request, 'forgot-password.html')
