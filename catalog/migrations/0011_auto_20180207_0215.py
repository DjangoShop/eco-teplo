# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-06 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20180207_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categorysub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.SubCategory', verbose_name='Подкатегория'),
        ),
    ]
