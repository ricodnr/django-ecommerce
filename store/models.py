from django.db import models
from django.urls import reverse


# Create your models here.
class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager,self).get_queryset().exclude(stock=0)
    
class ShopeeItem(models.Model):
    itemid= models.BigIntegerField(primary_key=True)
    shopid= models.BigIntegerField()
    currency= models.CharField(max_length=100, null=True, blank=True)
    name= models.CharField(max_length=255, null=True, blank=True)
    stock= models.BigIntegerField(null=True,blank=True)
    sold= models.BigIntegerField(null=True,blank=True)
    historical_sold= models.BigIntegerField(null=True,blank=True)
    liked_count= models.BigIntegerField(null=True,blank=True)
    brand= models.CharField(max_length=255, null=True, blank=True)
    cmt_count= models.BigIntegerField(null=True,blank=True)
    item_status= models.CharField(max_length=255, null=True, blank=True)
    price= models.BigIntegerField(null=True,blank=True)
    price_min= models.BigIntegerField(null=True,blank=True)
    price_max= models.BigIntegerField(null=True,blank=True)
    price_before_discount= models.BigIntegerField(null=True,blank=True)
    show_discount= models.BigIntegerField(null=True,blank=True)
    raw_discount= models.BigIntegerField(null=True,blank=True)
    is_official_shop= models.CharField(max_length=100, null=True, blank=True)
    avatar= models.CharField(max_length=255, null=True, blank=True)
    shop_location= models.CharField(max_length=255, null=True, blank=True)
    manager = ItemManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product", kwargs ={"pk":self.pk})
    
    
class ItemImage(models.Model):
    itemid = models.ForeignKey(ShopeeItem, on_delete=models.CASCADE, related_name='images')
    image = models.CharField(max_length=150,null=True,blank=True)


