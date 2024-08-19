from django.db import models
CATEGORY_CHOICES=(
  ('CR','Curd'),
  ('ML','Milk'),
  ('LS','Lassi'),
  ('GH','Ghee'),
  ('MS','Milkshake'),
  ('PN','Paneer'),
  ('CZ','Cheese'),
  ('IC','Icecreams'),

)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='' )
    prodapp=models.TextField(default="")
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self): 
        return self.title

class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
''' @property
    def totalamount(self):
        return self.quantity * self.product.discountrd_price'''
# Create your models here.
