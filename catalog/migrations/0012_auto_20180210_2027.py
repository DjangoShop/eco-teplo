# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180207_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(verbose_name='Доступен'),
        ),
    ]
