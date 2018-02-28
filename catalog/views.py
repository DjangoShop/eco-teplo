#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from catalog.models import Product, Category
from catalog.admin import ProductAdmin
from django.views.generic import ListView, DetailView
from django.conf.urls import url
from django.db.models import Q

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

class productView(DetailView):
    model = Product
    template_name = 'catalog/allCatalog/BaseProduct.html'
    context_object_name = 'product'  # Default: object_list


class search(ListView):
    model = Product
    paginate_by = 14
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super(ListView, self).get_queryset()
        q = self.request.GET.get("q")
        # q_lst2 = re.sub('ы', '', q)
        
        
        q_lst2 = q.replace('ы', '')
        # q_lst3 = q[0:-1].replace('е', 'й')
        q_lst = q.split(' ')
        
        # q_lst2 = re.sub(r"[ы]", "", q)
        if q or q_lst or q_lst2:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__icontains=q) |
                                Q(name__in=q_lst) |
                                 Q(name__icontains=q_lst2) |
                                  # Q(name__in=q_lst3) |

                                    Q(brand__name__icontains=q) |
                                     Q(brand__name__in=q_lst) |
                                      Q(brand__name__icontains=q_lst2) |

                                        Q(category__name__icontains=q) |
                                         Q(category__name__in=q_lst) |
                                          Q(category__name__icontains=q_lst2) |

                                                Q(categorysub__name__icontains=q) |
                                                 Q(categorysub__name__in=q_lst) |
                                                  Q(categorysub__name__icontains=q_lst2))
        
        
        elif q == 'пока':
            queryset = Product.objects.all().order_by('price').filter(category='4', categorysub='10')

        
        # TODO сделать название всех товаров, категорий, брендов и подкатегорий с маленькой буквы
        # не использовать букву ё в названиях
        # сделать чтобы он работал и во множественном числе тоже

        # FIXME довести поиск до ума, чтобы он мог работать с любой ересью от юзера

