from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'facebook': 'https://facebook.com'}
    return render(request, 'index.html', context)


def analyzer(request):
    data = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    analyzed = ''
    count = 0
    for chr in data:
        if chr == 'a':
            count += 1
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for chr in data:
            if chr not in punctuations:
                analyzed = analyzed + chr
        context = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed, 'no_of_a': count}
        #return render(request, 'analyze.html', context)
        data = analyzed
    if capitalize == 'on':
        analyzed = data.capitalize()
        context = {'purpose': 'Capitalize first', 'analyzed_text': analyzed, 'no_of_a': count}
        #return render(request, 'analyze.html', context)
        data = analyzed
    if fullcaps == 'on':
        analyzed = data.upper()
        context = {'purpose': 'Capitalize String', 'analyzed_text': analyzed, 'no_of_a': count}
        #return render(request, 'analyze.html', context)
        data = analyzed
    if newlineremove == 'on':
        for chr in data:
            if chr != '\n':
                analyzed = analyzed + chr
        context = {'purpose': 'New line remover', 'analyzed_text': analyzed, 'no_of_a': count}
        #return render(request, 'analyze.html', context)
        data = analyzed
    elif(newlineremove != 'on' and fullcaps != 'on' and capitalize != 'on' and removepunc != 'on'):
        return HttpResponse('Error')
    return render(request, 'analyze.html', context)


'''def capitalize(request):
    return HttpResponse("Capitalize first character")


def newlineremove(request):
    return HttpResponse("Newline remover")


def spaceremove(request):
    return HttpResponse("Space remover")


def charcount(request):
    return HttpResponse("Count all character ")'''