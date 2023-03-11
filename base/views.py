import gspread
import json
import requests

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def index(request):                                                         / for testing 
#     return HttpResponse("Hello, world. You're at the _base_ index.")        / for testing 

def askGpt(task,content,language):
    input = {"task":task, "text":content, "language":language}
    input = json.dumps(input)

    url = "https://script.google.com/macros/s/AKfycbx_uPIrQMMoLMi4YOkIyU8nHGgcFUZIPO1Vkk6soo4a1AdVVl6Rzb-fJ7a7ifzTujc/exec"
    response = requests.post(url, json=input)
    print(repsonse)