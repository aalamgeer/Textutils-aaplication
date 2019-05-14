from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product
from math import ceil

# Create your views here.
def index(request):
    #product = Product.objects.all()
    #n = len(product)
    #nslides = n//4 + ceil((n/4)-(n//4))
    allprod = []
    cateprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cateprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprod.append([prod, range(1,nslides), nslides])
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

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
