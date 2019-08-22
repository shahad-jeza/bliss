from django.contrib import admin
from .models import Category, products

# Register your models here.
admin.site.register(Category)
admin.site.register(products)