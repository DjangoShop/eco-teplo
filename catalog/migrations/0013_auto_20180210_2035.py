# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20180210_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступен'),
        ),
    ]
