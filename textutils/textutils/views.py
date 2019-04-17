from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'facebook': 'https://facebook.com'}
    return render(request, 'index.html', context)


def analyzer(request):
    data = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
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
        return render(request, 'analyze.html', context)
    elif capitalize == 'on':
        analyzed = data.capitalize()
        context = {'purpose': 'Capitalize first', 'analyzed_text': analyzed, 'no_of_a': count}
        return render(request, 'analyze.html', context)
    elif fullcaps == 'on':
        analyzed = data.upper()
        context = {'purpose': 'Capitalize String', 'analyzed_text': analyzed, 'no_of_a': count}
        return render(request, 'analyze.html', context)
    elif newlineremove == 'on':
        for chr in data:
            if chr != '\n':
                analyzed = analyzed + chr
        context = {'purpose': 'New line remover', 'analyzed_text': analyzed, 'no_of_a': count}
        return render(request, 'analyze.html', context)
    else:
        return HttpResponse('Error')


'''def capitalize(request):
    return HttpResponse("Capitalize first character")


def newlineremove(request):
    return HttpResponse("Newline remover")


def spaceremove(request):
    return HttpResponse("Space remover")


def charcount(request):
    return HttpResponse("Count all character ")'''