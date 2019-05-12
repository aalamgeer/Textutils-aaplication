from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product
from math import ceil

# Create your views here.
def index(request):
    product = Product.objects.all()
    print(product)
    n = len(product)
    nslides = n//4 + ceil((n/4)-(n//4))
    #prams = {"noSlides": nslides, "range": range(nslides), "product": product}
    allprod = [[product, range(1, len(product)), nslides],
               [product, range(1, len(product)), nslides]]
    prams = {'allprod': allprod}
    return render(request, 'nicebuy/index.html', prams)


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
