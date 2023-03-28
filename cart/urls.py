from django.urls import path
from .views import CartReview, CartAdd, CartDel, CartUpdate
app_name = 'cart'
urlpatterns = [
    path('',CartReview,name='cart'),
    path('add/',CartAdd,name='cartadd'),
    path('del/',CartDel, name='cartdel'),
    path('update/',CartUpdate, name='cartup'),
]