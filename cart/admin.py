# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cart,CartItem
# Register your models here.


admin.site.register(Cart)
admin.site.register(CartItem)
