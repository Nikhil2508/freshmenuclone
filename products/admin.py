from django.contrib import admin

# Register your models here.
from .models import Product,ProductCategories



admin.site.register(Product)
admin.site.register(ProductCategories)
