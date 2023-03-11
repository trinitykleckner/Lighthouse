from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Page



# Create your views here.
# def index(request):
#     return HttpResponse("Hello TEST!!!!!")


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


# ...
# def detail(request):
#     page = get_object_or_404(Page, pk=1)
#     return render(request, 'polls/detail.html', {'page': page})



