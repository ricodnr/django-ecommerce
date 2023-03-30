from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, CreateView, FormView
from .cart import Cart
from .models import Order, OrderItem
from .forms import OrderForm
from store.models import ShopeeItem
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sessions.backends.db import SessionStore
# Create your views here.

# def CartReview(request):
#     cart = Cart(request)
#     return render(request, 'cart.html', {'cart': cart})

class CartReview(FormView):
    form_class = OrderForm
    template_name='cart.html'

    def form_valid(self,form):
        cart = Cart(self.request)
        ttc = cart.get_total_price()
        data = form.cleaned_data
        session_id = self.request.session.session_key
        if Order.objects.filter(orderid=session_id).exists():
            ordering = Order.objects.filter(orderid=session_id).update(
                name=data['name'],
                address=data['address'],
                email=data['email'],
                totalcost=int(ttc),
            )
            order = Order.objects.get(orderid=session_id)
        else:
            order = Order.objects.create(name=data['name'],
                                        address=data['address'],
                                        email=data['email'],
                                        totalcost=int(ttc),
                                        orderid=session_id)
            for item in cart:
                OrderItem.objects.create(order_id=order.pk,
                                        itemid=item['product'],
                                        price=item['price'],
                                        quantity=item['qty'],
                                        subtotal=int(item['price'])*int(item['qty'])
                                        )
        domain = get_current_site(self.request).domain
        link = "https://"+domain + f"/cart/complete/{order.orderid}"
        title = f"Order #{order.pk} confirm email"
        message = f"Please click the link below to confirm your order {order.pk} ship to {order.address}, {order.name}\n{link} "
        send_mail(
            title,
            message,
            'settings.EMAIL_HOST_USER',
            [order.email]
        )
        self.request.session.flush()
        return redirect('cart:cart_con',order.pk)

class CartConfirm(DetailView):
    model = Order
    template_name = 'cart_confirm.html'

    def post(self,request):
        order = self.get_object()
        
class CartComplete(DetailView):
    model = Order
    template_name = 'cart_complete.html'

    def get_object(self,queryset=None):
        return Order.objects.get(orderid=self.kwargs.get("orderid"))
        
        
    

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
        c = cart.cart_item_check(reqitemid)
        if c:
            cart.delete(item=reqitemid)
            nqty = cart.__len__()
            resp = JsonResponse({'qty':nqty,'itemqty':"Removed from Cart"})
        else: 
            nqty = cart.__len__()
            resp = JsonResponse({'qty':nqty,'itemqty':"Item not in Cart"})
    return resp


