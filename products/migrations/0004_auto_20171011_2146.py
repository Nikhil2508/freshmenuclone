# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='products.ProductCategories'),
        ),
    ]