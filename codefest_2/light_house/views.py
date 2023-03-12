from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Page

import json
import requests

indexDict = {0: [1,2,3],
                 1: [4,5],
                 2:[6,7],
                 3:[8,9,10]}
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

def options(request, file, index=-1):
    print("LANGUAGE",request.session['language'])
    request.session['index'] = index
    page = Page.objects.order_by('-id')[index]
    pageDict = page.toDict()
    ops = page.getOptions()

    if request.session['language'] not in ["english", "null", None]:
        pageDict = translateDict(pageDict,request.session['language'])
        ops = list(map(lambda x: askGpt("translate",x,request.session['language']),ops))
    return render(request, 'light_house/'+file+'.html', {"page":pageDict,"options":page.getOptions(),"indexes":indexDict[index]})

def endpoint(request, index, task="list"):
    print("HEREEEE",Page.objects.order_by('header'))
    page = Page.objects.order_by('id')[index]
    pageDict = page.toDict()
    if request.session['language'] not in ["english", "null", None]:
        pageDict = translateDict(pageDict,request.session['language'])
    if request.session['state'] == None:
        gpt = askGpt(task,page.content2[4:],request.session['language'])
    else:
        gpt = askGpt(task,page.content2[4:]+"in "+request.session['state'],request.session['language'])
    gpt = list(map(lambda x: x[0], gpt))
    # print("HEREEEEE",gpt)
    return render(request, 'light_house/endpoint.html', {"page":page.toDict(),"response":gpt})

def final(request):
    return render(request, 'light_house/final.html', {})

def now(request): return options(request, "now", 0)
def documentation(request): return options(request, "documentation", 2)
def settling(request): return options(request, "settling", 3)

def food(request): return endpoint(request, 4) 
def shelter(request): return endpoint(request, 5)
def id(request): return endpoint(request, 6)
def ssn(request): return endpoint(request, 10)
def jobs(request): return endpoint(request, 7)
def school(request): return endpoint(request, 9)
def community(request): return endpoint(request, 8, "ask")

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
