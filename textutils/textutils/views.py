from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'facebook': 'https://facebook.com'}
    return render(request, 'index.html', context)


def removepunc(request):
    print(request.GET.get('text'))
    data = request.POST.get('text')
    print(data)
    return HttpResponse("Remove punctuation")


def capitalize(request):
    return HttpResponse("Capitalize first character")


def newlineremove(request):
    return HttpResponse("Newline remover")


def spaceremove(request):
    return HttpResponse("Space remover")


def charcount(request):
    return HttpResponse("Count all character ")