from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Anasayfaya hoş geldiniz")
   
   context=dict()
   return render(request, "index/index.html", context)

# Create your views here.

def about(request):
   context=dict()
   return render(request, "index/about.html", context)

def blog(request):
   context=dict()
   return render(request, "index/blog.html", context)

def works(request):
   context=dict()
   return render(request, "index/works.html", context)

def contact(request):
   context=dict()
   return render(request, "index/contact.html", context)

def docs(request):
   context=dict()
   return render(request, "index/docs.html", context)
