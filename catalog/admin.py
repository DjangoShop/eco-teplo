# -*- coding: utf-8 -*-
from django.contrib import admin
from catalog.models import *


# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name'] # , 'slug']
    # prepopulated_fields = {'slug': ('name', )}

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'name', 'category', 'categorysub', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'brand', 'category', 'categorysub']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    # search_fields = ['brand__icontains', 'name__icontains']
    

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name'] # , 'slug']
    # prepopulated_fields = {'slug': ('name', )}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)