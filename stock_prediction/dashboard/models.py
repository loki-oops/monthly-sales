from django.db import models


# Create your models here.

class Order(models.Model):
    product_catagory = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_prise = models.DecimalField(max_digits=10, decimal_places=2)
