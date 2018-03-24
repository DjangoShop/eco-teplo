# -*- coding: utf-8 -*-
from django.db import models, migrations
from django.core.urlresolvers import reverse


# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Категория")
    # slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name="Псевдоним")
    # blank=True, чтобы сделать поле необязательным для заполнения

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    

    def __str__(self):    
        return self.name

    
# Модель подкатегории
class SubCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True, blank=True, verbose_name="Подкатегория")

    class Meta:
        ordering = ['name']
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    

    def __str__(self):    
        return self.name

   
# Модель бренда
class Brand(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name="Бренд")

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    

    def __str__(self):    
        return self.name

   


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    categorysub = models.ForeignKey(SubCategory, null=True, blank=True, verbose_name="Подкатегория")
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=100, db_index=True, verbose_name="Псевдоним")
    image = models.ImageField(upload_to='static/products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    brand = models.ForeignKey(Brand, related_name='products', null=True, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Цена")
    # new_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена с процентом")
    stock = models.PositiveIntegerField(verbose_name="На складе") # TODO заставить при покупке уменьшаться этот счетчик
    # FIXME если Юре понравится идея со скидками или акциями, то сделать здесь поле, как с доступностью товара
    # Так же помимо вывода подобного товара в главный каталог, зделать в шаблоне для него отдельную ссылку "Скидки" или "Акции"
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления") 

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('catalog:ProductDetail', args=[self.id, self.slug])