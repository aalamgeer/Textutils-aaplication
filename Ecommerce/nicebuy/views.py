from django.shortcuts import render
from django.http import HttpResponse
from .models import  Product, Contact
from math import ceil

# Create your views here.
def index(request):
    #product = Product.objects.all()
    #n = len(product)
    #nslides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    cateprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in cateprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nslides), nslides])
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]

    prams = {'allProds': allProds}
    return render(request, 'nicebuy/index.html', prams)


def about(request):
    return render (request, 'nicebuy/about.html')


def contact(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('description')
        contact = Contact(name=name, email=email, phone=phone, desc=message)
        contact.save()
    return render (request, 'nicebuy/contact.html')


def tracker(request):
    return render (request, 'nicebuy/tracker.html')


def search(request):
    return render (request, 'nicebuy/search.html')


def productView(request, prodId):
    #get product using view
    product = Product.objects.filter(id=prodId)
    print(product)
    return render (request, 'nicebuy/productview.html', { "product" :product[0] } )


def checkout(request):
    return render (request, 'nicebuy/index.html')
