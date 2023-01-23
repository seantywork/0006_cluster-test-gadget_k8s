from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from . import models
import json

def ready(request):
    r = 1
    return HttpResponse("Under Maintenance")

def passme(request):
    context = {}
    return HttpResponse(render(request,'index.html',context))

def sendme(request):

    post_dict = json.loads(request.body)
    
    x = post_dict["query"]
    x = str(x)
    y = post_dict["psw"]
    y = str(y)

    context = models.searchengine(x,y)

    return JsonResponse(context)



