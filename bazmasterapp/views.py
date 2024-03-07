from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'auth.html')


def main(request):
    return render(request, 'main.html', context={'summary': 1000})
    # return render(request, 'test.html')


def auth(request):
    return render(request, 'auth.html')
