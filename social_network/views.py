# social_network/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'social_network/index.html')


# Create your views here.
