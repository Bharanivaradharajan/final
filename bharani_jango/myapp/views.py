from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


def home(request):
    return render(request,"home.html")
def books(request):
    return render(request,"books.html")
def social(request):
    return render(request,"social.html")
def doctor(request):
    return render(request,"doctor.html")
def reference(request):
    return render(request,"reference.html")
def forms(request): 
    return render(request,"forms.html")
def ebooks(request):
    return render(request,"ebooks.html")
