from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def app1_index(request):
    return HttpResponse("<h1>Hello, world!. You're at the app1 index</h1>")