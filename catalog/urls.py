#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from catalog.models import Product
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #Main category 
    # url(r'^allCatalog.html$', ListView.as_view(queryset=Product.objects.all().filter(category='5'), template_name='catalog/allCatalog/allCatalog.html')),
    # filter(category='5') это фильтрация товаров по id категорий, которуые нужно отобразить
    # TODO сделать то же самое для остальных категорий 


   
    # search
    url(r'^catalog_search/$', views.search.as_view(), name='catalog_search'),
    
    # Main category 
    url(r'^allCatalog/$', views.all_catalog.as_view(), name='all_catalog'),# ListView.as_view(queryset=Product.objects.all().order_by('price'), template_name='catalog/allCatalog/allCatalog.html')), # все категории
     # category accessories for floors
    
   
    # category conditioners
  
   
   
    url(r'^previewWarmFloors.html$', views.all_floors_preview, name='all_catalog_preview'),
    # category floors
    # url(r'^catalogAllFloors.html$', views.all_floors.as_view(), name='all_floors'), # теплый пол 
    url(r'^catalogInfrared.html$', views.catalog_infrared.as_view(), name='catalog_infrared'), # теплый пол плёночный

    url(r'^catalogMatsDevi.html$', views.catalog_mats_devi.as_view(), name='catalog_mats_devi'), # теплый пол нагревательный мат
    url(r'^catalogCableDevi.html$', views.catalog_cable_devi.as_view(), name='catalog_cable_devi'), # теплый пол кабельный

    url(r'^catalogMatsArnodlRak.html$', views.catalog_mats_arnodlrak.as_view(), name='catalog_mats_arnodlrak'),
    url(r'^catalogCableArnodlRak.html$', views.catalog_cable_arnodlrak.as_view(), name='catalog_cable_arnodlrak'),
    
    url(r'^previewAccessories.html$', views.all_accessories_preview, name='all_accessories_preview'),
    
    url(r'^accessoriesThermostats.html$', views.accessories_thermostats.as_view(), name='accessories_thermostats'), 
    url(r'^accessoriesMountingKit.html$', views.accessories_mounting_kit.as_view(), name='accessories_mounting_kit'),
    url(r'^accessoriesThermalInsulation.html$', views.accessories_thermal_insulation.as_view(), name='accessories_thermal_insulation'),
   

    url(r'^previewAllCond.html$', views.all_conditioners_preview, name='all_conditioners_preview'),

    url(r'^splitSystem.html$', views.conditioners_split.as_view(), name='conditioners_split_system'),
    url(r'^invertorSystem.html$', views.conditioners_invertor.as_view(), name='conditioners_invertor_system'),
   
   
   
    # url(r'^allCatalog/(?P<slug>[-\w]+).html', DetailView.as_view(model = Product, template_name='catalog/allCatalog/BaseProduct.html')),
    
    url(r'^allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    
    url(r'^accessoriesFloors/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^conditioners/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),

    # search url
    url(r'^catalog_search/allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^catalog_search/accessoriesFloors/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^catalog_search/conditioners/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),



    url(r'^warmFloors/All/allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^warmFloors/infraredFilm/allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^warmFloors/heatingMats/allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),
    url(r'^warmFloors/cable/allCatalog/(?P<slug>[-\w]+).html', views.productView.as_view(), name='product'),





   
   

    # url(r'^allCatalog.html', views.all_catalog, name='all_catalog'),
   
    # url(r'^allCatalog/tyoplyj-pol-kabelnyj-140-vt-71-m.html', template_name='catalog/allCatalog/tyoplyj-pol-kabelnyj-140-vt-71-m.html'),

    # url(r'^(!P<pk\d+)$', DetailView.as_view(model = Product, template_name='catalog/allCatalog/BaseProduct.html')),
    

    # url(r'^accessoriesFloors/catalogAllAccess.html', views.all_accessories, name='all_accessories'),
    # url(r'^conditioners/catalogAllCond.html', views.all_conditioners, name='all_conditioners'),

    # category floors
    # url(r'^warmFloors/All/catalogAllFloors.html', views.all_floors, name='all_floors'),
    # url(r'^warmFloors/infraredFilm/catalogInfrared.html', views.catalog_infrared, name='catalog_infrared'),
    # url(r'^warmFloors/heatingMats/catalogMats.html', views.catalog_mats, name='catalog_mats'),
    # url(r'^warmFloors/cable/catalogCable.html', views.catalog_cable, name='catalog_cable'),

   

    # url(r'^BaseProduct.html', views.ProductDetail, name='ProductDetail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 