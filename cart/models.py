# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.


class CartItem(models.Model):
    cartNone = models.ForeignKey("Cart",null=True,blank=True)
    item = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)


    def __unicode__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    items = models.ManyToManyField(CartItem)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)
