from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ShopeeItem as Item, ItemImage
from cart.cart import Cart
# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Item

    

class ProductView(DetailView):
    template_name = 'product.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        price = self.object.price
        context['related'] = Item.manager.filter(price__lte=price+50000,price__gte=price-50000).exclude(itemid=self.object.itemid)[:4]
        return context