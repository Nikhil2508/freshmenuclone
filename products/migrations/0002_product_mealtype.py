# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mealType',
            field=models.CharField(choices=[('V', 'Veg meal'), ('NV', 'Non-Veg meal')], default='V', max_length=2),
            preserve_default=False,
        ),
    ]
