from django.shortcuts import render

from django.http.response import HttpResponse
# Create your views here.

def getPostsList(request):
    return HttpResponse("<h1> Post Lists </h1>")

def getHome(request):
    return render(request , template_name='post/home.html')

