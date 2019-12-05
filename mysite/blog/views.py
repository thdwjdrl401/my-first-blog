from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html', {})

def Bongpyeong(request):
    return render(request, 'blog/Bongpyeong.html', {})

def inje(request):
    return render(request, 'blog/inje.html', {})

def jinhae(request):
    return render(request, 'blog/jinhae.html', {})

def gangreung(request):
    return render(request, 'blog/gangreung.html', {})