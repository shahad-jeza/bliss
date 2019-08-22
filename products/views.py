from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Category, products
from django.template import RequestContext




# home page

def home_page(request):
	return render(request, "home.html", {})

# catigories 

# products

# privecy
def privecy(request):
	return render(request, "privecy.html", {} )