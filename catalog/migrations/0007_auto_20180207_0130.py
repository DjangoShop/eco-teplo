# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-06 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180207_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Псевдоним'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Псевдоним'),
        ),
        migrations.AlterField(
            model_name='category',
            name='subname',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Подкатегория'),
        ),
    ]
