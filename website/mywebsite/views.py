from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title': 'website Kematian',
        'heading': 'Selamat Datang Di Website Kematian',
        'subheading': 'INI WEBSITE KEMATIAN'
    }
    return render(request, 'index.html', context)

