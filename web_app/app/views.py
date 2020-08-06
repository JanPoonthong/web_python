from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app/index.html")

def jan(request):
    return HttpResponse("Hello, Jan!")

def devon(request):
    return HttpResponse("Hello, Devon!")

def greet(request, name):
    return render(request, "app/greet.html", {
        "name": name.capitalize()
    })
