from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseNotFound
from django.core.serializers.json import DjangoJSONEncoder
from pathlib import Path
from .models import Q, I, IT
import json

# Create your views here.

BASE = Path(__file__).resolve().parent

def load_translation(name):
    path = BASE / "lang" / f"{name}.json"
    with path.open(encoding="utf-8") as f:
        return json.load(f)

lgs = {
    "eng": load_translation("eng"),
    "rus": load_translation("rus")
}

def custom_404(request, exception):
    return HttpResponseNotFound(render(request, 'home.html'))

def main(request):
    template = loader.get_template("main.html")
    context = {
        'lgs': lgs
    }
    return HttpResponse(template.render(context, request))

def question(request):
    template = loader.get_template("question.html")  
    qs = Q.objects.all().values('id', 'n', 'rus', 'eng')
    qs_json = json.dumps(list(qs), cls=DjangoJSONEncoder)
    context = {
        'qs_json': qs_json,
        'lgs': lgs
    }
    return HttpResponse(template.render(context, request))

def result(request):
    template = loader.get_template("result.html")
    ids = I.objects.all().values('id', 'c', 'x', 'y', 'w', 'h')
    ivs = IT.objects.all().values('id', 'q', 'rus', 'eng')
    is_json = json.dumps(list(ids), cls=DjangoJSONEncoder)
    iv_json = json.dumps(list(ivs), cls=DjangoJSONEncoder)
    context = {
        'is_json': is_json,
        'iv_json': iv_json,
        'lgs': lgs
    }  
    return HttpResponse(template.render(context, request))



