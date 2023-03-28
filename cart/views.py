from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .cart import Cart
from store.models import ShopeeItem
from django.http import JsonResponse
from django import template
register = template.Library()
# Create your views here.

def CartReview(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def CartAdd(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        reqitemid = int(request.POST.get('itemid'))
        reqqty = int(request.POST.get('qty'))
        reqitem = get_object_or_404(ShopeeItem, itemid=reqitemid)
        cart.add(reqitem,reqqty)
        cartqty = cart.__len__()
        itemqty = cart.stock_check(reqitemid)
        stock = reqitem.stock
        if int(itemqty) == stock : 
            if stock == 1:
                resp = JsonResponse({'qty':cartqty, 'itemqty':f"{itemqty} in Cart", 'stock': f"Only {stock} item available"})
            else: resp = JsonResponse({'qty':cartqty, 'itemqty':f"{itemqty} in Cart", 'stock': f"Only {stock} items available"})
        else:
            resp = JsonResponse({'qty':cartqty, 'itemqty':f"{itemqty} in Cart", 'stock': ""})
        return resp

def CartUpdate(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        reqitemid = request.POST.get('itemid')
        reqqty = request.POST.get('qty')
        reqitem = get_object_or_404(ShopeeItem, itemid=int(reqitemid))
        cart.update(reqitem,reqqty)
        cartqty = cart.__len__()
        itemqty = cart.stock_check(reqitemid)
        resp = JsonResponse({'qty':cartqty, 'itemqty':f"{itemqty} in Cart"})
        return resp

def CartDel(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        reqitemid = int(request.POST.get('itemid'))
        cart.delete(item=reqitemid)
        nqty = cart.__len__()
        totalcost = cart.get_total_price()
        resp = JsonResponse({'qty':nqty,'total':totalcost})
    if request.POST.get('action') == 'postfromproduct':
        reqitemid = int(request.POST.get('itemid'))
        cart.delete(item=reqitemid)
        nqty = cart.__len__()
        resp = JsonResponse({'qty':nqty,'itemqty':"Removed from Cart"})
    return resp


