from django.db import models
from store.models import ShopeeItem
from django.urls import reverse
from django.contrib.sessions.models import Session
import uuid
# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=False,blank=False)
    totalcost = models.BigIntegerField()
    is_odered = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    orderid = models.CharField(max_length=100,unique=True)

    def get_absolute_url(self):
        return reverse('cart:cart_con',kwargs={'pk':self.pk})
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="items")
    itemid = models.ForeignKey(ShopeeItem, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.BigIntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.itemid)
    
