from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY = {
        "ELECTRONICS" : "electronics",
        "FASHION" : "fashion",
        "GROCERY" : "grocery",
    }
    sku = models.CharField(max_length=18, unique=True)
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=20, choices=[(key, value) for key, value in CATEGORY.items()])

    price = models.DecimalField(max_digits = 20, decimal_places=2)
    quantity = models.IntegerField()

    
