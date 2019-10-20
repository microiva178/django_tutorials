from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'homepage/homepage.html')

def page_1(request):
    return render(request, 'homepage/page_1.html')

def page_2(request):
    return render(request, 'homepage/page_2.html')


