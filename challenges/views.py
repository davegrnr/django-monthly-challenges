from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("Eat no meat for the entire month")


def february(request):
    return HttpResponse("Run 30 miles")


def march(request):
    return HttpResponse("Learn Django for 20 mins every day")
