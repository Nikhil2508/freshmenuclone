# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from products.models import Product
# Create your models here.


User = settings.AUTH_USER_MODEL



class OrderItems(models.Model):
    product = models.ForeignKey(Product)
    qty = models.IntegerField(default=1)


    def __str__(self):
        return str(self.id)

class Order(models.Model):
    user = models.ForeignKey(User)
    items = models.ManyToManyField(OrderItems)



    def __str__(self):
        return str(self.id)
