# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-15 17:56
from __future__ import unicode_literals

from django.db import migrations
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20180226_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(db_index=True, default='', editable=False, null=True, serialize=False),
        ),
        migrations.AddField(
            model_name='category',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(db_index=True, default='', editable=False, null=True, serialize=False),
        ),
        migrations.AddField(
            model_name='product',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(db_index=True, default='', editable=False, null=True, serialize=False),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(db_index=True, default='', editable=False, null=True, serialize=False),
        ),
    ]
