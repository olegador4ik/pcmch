from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseNotFound
from django.core.serializers.json import DjangoJSONEncoder
from .models import Q, I
import json

# Create your views here.

def custom_404(request, exception):
    return HttpResponseNotFound(render(request, 'home.html'))

def main(request):
    template = loader.get_template("main.html")
    context = {
    }
    return HttpResponse(template.render(context, request))

def question(request):
    template = loader.get_template("question.html")  
    qs = Q.objects.all().values('id', 'q', 'n')
    qs_json = json.dumps(list(qs), cls=DjangoJSONEncoder)
    context = {
        'qs_json': qs_json
    }
    return HttpResponse(template.render(context, request))

def result(request):
    template = loader.get_template("result.html")
    ids = I.objects.all().values('id', 'n', 'c', 'x', 'y', 'w', 'h')
    is_json = json.dumps(list(ids), cls=DjangoJSONEncoder)
    context = {
        'is_json': is_json 
    }  
    return HttpResponse(template.render(context, request))



