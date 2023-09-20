# social_network/views.py
from django.shortcuts import render

def index(request):
    return render(request, "social_network/index.html")

def login(request):
    return render(request, "social_network/login.html")

def signup(request):
    return render(request, "social_network/signup.html")


# Create your views here.
