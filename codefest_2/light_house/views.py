from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Page



def index(request):
    page = Page.objects.order_by('-id')[0]
    return render(request, 'light_house/trial.html', {"page":page.toDict()})
    latest_question_list = Page.objects.order_by('-id')[:5]
    output = ', '.join([q.header for q in latest_question_list])
    return HttpResponse(output)

def options(request):
    return render(request, 'light_house/options.html', {})

def endpoint(request):
    return render(request, 'light_house/endpoint.html', {})

def final(request):
    return render(request, 'light_house/final.html', {})

def askGpt(task,content,language):
    input = {"task":task, "text":content, "language":language}

    url = "https://script.google.com/macros/s/AKfycbx_uPIrQMMoLMi4YOkIyU8nHGgcFUZIPO1Vkk6soo4a1AdVVl6Rzb-fJ7a7ifzTujc/exec"
    response = requests.post(url, json=input)
    response_dict = json.loads(response.text)
    return response_dict["translated"]
