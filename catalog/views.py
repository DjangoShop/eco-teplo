#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from django.http import HttpResponse, response
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from catalog.models import Product, Category
from catalog.admin import ProductAdmin
from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity


# Всем привет. Добавил в postgresql дополнение pg_trgm. В Django использую TrigramSimilarity, как совместить его с SearchVector
# TODO так же ИК пленочный пол продается по кв.м. максимум 100 кв.м

def all_floors_preview(request):
    return render(request, 'catalog/warmFloors/previewWarmFloors.html')

def all_accessories_preview(request):
    return render(request, 'catalog/accessoriesFloors/previewAccessories.html')

def all_conditioners_preview(request):
    return render(request, 'catalog/conditioners/previewAllCond.html')







class all_catalog(ListView):
    model = Product
    template_name = 'catalog/allCatalog/allCatalog.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    # FIXME посмотреть можно ли делать пагинацию для с фильтром для разных категорий
    # TODO сделать вместо верхнего меню три большие карточки с 3 главными категорями,
    # а уже под ними выводить акционные товары для привлечения внимания 
    queryset = Product.objects.all().order_by('price') #.filter(category='13') # выводит акционные товары 
    # фильтр для удаления отображения товара, если он не доступен .filter(available=True) 


# floors sub category 
# class all_floors(ListView):
#     model = Product
#     template_name = 'catalog/warmFloors/catalogAllFloors.html'   # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'product'  # Default: object_list
#     paginate_by = 9
#     queryset = Product.objects.all().order_by('price').filter(category='11')

class catalog_infrared(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='11', categorysub='2')

class catalog_mats_devi(ListView):
    model = Product
    template_name ='catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='11', categorysub='3', brand='1')
    
class catalog_cable_devi(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9 
    queryset = Product.objects.all().order_by('price').filter(category='11', categorysub='4', brand='1')


class catalog_mats_arnodlrak(ListView):
    model = Product
    template_name ='catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='11', categorysub='3', brand='5')

class catalog_cable_arnodlrak(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9 
    queryset = Product.objects.all().order_by('price').filter(category='11', categorysub='4', brand='5')


# def catalog_cable(request, url):
    

class accessories_thermostats(ListView):
    model = Product
    template_name =  'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='2', categorysub='5')

class accessories_mounting_kit(ListView):
    model = Product
    template_name =  'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='2', categorysub='8')

class accessories_thermal_insulation(ListView):
    model = Product
    template_name =  'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 9
    queryset = Product.objects.all().order_by('price').filter(category='2', categorysub='7')

# accessories for floors sub category


class conditioners_split(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 4
    queryset = Product.objects.all().order_by('price').filter(category='4', categorysub='9')

class conditioners_invertor(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product'  # Default: object_list
    paginate_by = 4
    queryset = Product.objects.all().order_by('price').filter(category='4', categorysub='10')


# conditioners sub category





# Страница товара 

# Страница товара
# def ProductDetail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'catalog/allCatalog/BaseProduct.html', {'product': product}) 

class productView(DetailView):
    model = Product
    template_name = 'catalog/allCatalog/BaseProduct.html'
    context_object_name = 'product'  # Default: object_list




class search(ListView):
    model = Product
    paginate_by = 14
    template_name = 'catalog/product_list.html'
    

    def get_queryset(self):
        
        # Получаем не отфильтрованный кверисет всех моделей
        #stop_words = ~SearchQuery(['и', 'при', 'а', 'для', 'в', 'на', 'из', 'которые', 'дешовый', 'специальные', 'недорогие', 'по', 'у', 'за', 'руб', 'рубли', 'рублей', 'кабель', 'пленка'])
        queryset = super(search, self).get_queryset()
        q = self.request.GET.get("q")

      
        
        
        #return queryset.annotate(search=SearchQuery(Q('brand__name')) | SearchQuery(Q('name'))).filter(search=q)
       
        
        if q: #or q_lst or q_lst2
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            # FIXME сделать фильтр по ценам
            # TODO Добавить в БД словарь стоп-слов
           
            
            #search_query = SearchQuery(q, config='russian')
             # search=q, config='russian') 
            #pre_search = Product.objects.annotate(similarity=TrigramSimilarity('name', q)).filter(similarity__gt=0.3).order_by('-similarity')
        
            #return queryset.annotate(similarity=vector_trgm).filter(similarity__gt=0.2).order_by('price')
             #.order_by('-similarity')
            
            vector = SearchVector('categorysub__name', 'brand__name', 'category__name', 'name', raw=True, fields=('name'))
            vector_trgm = TrigramSimilarity('categorysub__name', q, raw=True, fields=('name')) + TrigramSimilarity('brand__name', q, raw=True, fields=('name')) + TrigramSimilarity('category__name', q, raw=True, fields=('name')) + TrigramSimilarity('name', q, raw=True, fields=('name'))
            return queryset.annotate(search=vector).order_by('price').filter(search=q) or queryset.annotate(similarity=vector_trgm).filter(similarity__gt=0.2).order_by('price')

            

            
            # return queryset.order_by('price').filter(category='11', categorysub='4')
      # TODO сделать, что если q не находит рзультат, то обрабатывать обычным SearchVector
       # elif q == '':

        # return queryset.annotate(search=SearchVector('brand__name', 'name', 'category__name', 'categorysub__name')).order_by('price').filter(search=q)
            #return queryset.annotate(search=SearchVector('brand__name', 'name', 'category__name', 'categorysub__name')).order_by('price').filter(search=q)
            #return queryset.annotate(search=SearchVector('name')).order_by('price').filter(name__unaccent__startswith=q)
            #return queryset.annotate(search=SearchVector('brand__name', 'name', 'category__name', 'categorysub__name')).order_by('price').filter(search=stop_words)
     #       return Product.objects.search(q)
        elif not q:
             return queryset.order_by('price')

        # TODO сделать название всех товаров, категорий, брендов и подкатегорий с маленькой буквы
        # не использовать букву ё в названиях
        # сделать чтобы он работал и во множественном числе тоже

        # FIXME довести поиск до ума, чтобы он мог работать с любой ересью от юзера

