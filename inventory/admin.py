from django.contrib import admin

#from inventory.models import Product
from .models import Product
# Register your models here.

#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'category', 'price', 'quantity')
    search_fields = ('name', 'sku',)
    list_filter = ('category',)
    ordering = ('name',)


