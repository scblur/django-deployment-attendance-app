from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html", {})

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, "AppTwo/index.html",context=helpdict)
