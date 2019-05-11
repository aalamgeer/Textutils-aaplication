from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'nicebuy/index.html')


def about(request):
    return render (request, 'nicebuy/about.html')


def contact(request):
    return render (request, 'nicebuy/index.html')


def tracker(request):
    return render (request, 'nicebuy/index.html')


def search(request):
    return render (request, 'nicebuy/index.html')


def productView(request):
    return render (request, 'nicebuy/index.html')


def checkout(request):
    return render (request, 'nicebuy/index.html')
