from django.shortcuts import render

# Create your views here.
def app2_index(request):
    return HttpResponse("<h1>Hello, world!. You're at the app2 index</h1>")