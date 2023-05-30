from django.db import models
from ecommerceapp.models import Product

class Cart(models.Model):
    cartid=models.CharField(max_length=200,blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date_added']

    def __str__(self):
        return '{}'.format(self.cartid)


class Cartitem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartitems'

    def total(self):
        return self.product.price*self.quantity

    def __str__(self):
        return '{}'.format(self.product)



