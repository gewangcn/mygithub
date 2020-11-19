from django.http import HttpResponse
from django.shortcut import redirect

def index(request):
    return HttpResponse('hello github')

def login(request):
    return redirct('/index')
