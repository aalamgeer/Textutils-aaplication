from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'facebook': 'https://facebook.com'}
    return render(request, 'index.html', context)


def analyzer(request):
    print(request.GET.get('text'))
    data = request.GET.get('text')
    removepunc = request.POST.get('removepunc', 'off')
    analyzed = data
    context = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', context)


'''def capitalize(request):
    return HttpResponse("Capitalize first character")


def newlineremove(request):
    return HttpResponse("Newline remover")


def spaceremove(request):
    return HttpResponse("Space remover")


def charcount(request):
    return HttpResponse("Count all character ")'''