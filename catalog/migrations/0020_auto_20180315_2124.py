# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-15 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20180315_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([]),
        ),
    ]
