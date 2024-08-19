from django.contrib import admin
from . models import Product,Cart
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','product','quantity']
# Register your models here.
