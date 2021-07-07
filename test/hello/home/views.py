from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")
    
def contact(request):
    return HttpResponse("This is contacts page")