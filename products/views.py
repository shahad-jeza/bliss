from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Category, products
from django.template import RequestContext




# home page

def home_page(request , **kwargs):
	queryset= products.objects.filter(skin_type='all skin types')
	return render(request, "home.html", {'queryset' : queryset})

# catigories 

# products(shop all)
def shop_all(request):
	catalog = products.objects.all()
	return render(request, "shop_all.html", {'catalog' : catalog} )


# privecy
def privecy(request):
	return render(request, "privecy.html", {} )

def terms(request):
	return render(request, "terms.html", {} )