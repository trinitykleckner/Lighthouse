from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Page

import json
import requests


def index(request):
    request.session['language'] = request.GET.get("language")
    request.session['state'] = request.GET.get("state")
    request.session['county'] = request.GET.get("county")
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    page = Page.objects.order_by('id')[0]
    return render(request, 'light_house/index.html', {"page":page.toDict(),"options":page.getOptions(),"language":request.session['language']}) # changed options.html to index.html (Ahmed)
    # latest_question_list = Page.objects.order_by('-id')[:5]
    # output = ', '.join([q.header for q in latest_question_list])
    # return HttpResponse(output)

def language(request):
    return render(request, 'light_house/languageAndLocation.html', {})

def options(request, index=0):
    page = Page.objects.order_by('-id')[index]
    pageDict = translateDict(page.toDict(),request.session['language'])
    ops = map(lambda x: askGpt("translate",x,request.session['language']),page.getOptions())
    return render(request, 'light_house/options.html', {"page":pageDict,"options":page.getOptions()})

def endpoint(request, index):
    page = Page.objects.order_by('-id')[index]
    pageDict = translateDict(page.toDict(),request.session['language'])
    gpt = askGpt("ask",page.content2[3:],request.session['language'])
    return render(request, 'light_house/endpoint.html', {"page":page.toDict(),"response":gpt})

def final(request):
    return render(request, 'light_house/final.html', {})

def translateDict(dict, language):
    translated = {}
    for key in dict:
        translated[key] = askGpt("translate",dict[key],language)
    return translated

def askGpt(task,content,language):
    input = {"task":task, "text":content, "language":language}

    url = "https://script.google.com/macros/s/AKfycbx_uPIrQMMoLMi4YOkIyU8nHGgcFUZIPO1Vkk6soo4a1AdVVl6Rzb-fJ7a7ifzTujc/exec"
    response = requests.post(url, json=input)
    response_dict = json.loads(response.text)
    return response_dict["translated"]
