from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Product(models.Model):
    MEAL_TYPES = (('V',"Veg meal"),('NV',"Non-Veg meal"),)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_price = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    mealType = models.CharField(max_length=2, choices=MEAL_TYPES)
    category = models.ManyToManyField('ProductCategories',blank=True,null=True)



    def __str__(self):
        return self.title


class ProductCategories(models.Model):
    title = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
