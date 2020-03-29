from django.http import HttpResponse
from django.shortcuts import render

# /polls -> index
def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")


def news(request):
    return HttpResponse('News')