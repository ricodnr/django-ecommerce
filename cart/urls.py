from django.urls import path
from .views import CartReview, CartAdd, CartDel, CartUpdate, CartConfirm, CartComplete
app_name = 'cart'
urlpatterns = [
    path('',CartReview.as_view(),name='cart'),
    path('add/',CartAdd,name='cartadd'),
    path('del/',CartDel, name='cartdel'),
    path('update/',CartUpdate, name='cartup'),
    path('confirm/<int:pk>',CartConfirm.as_view(),name='cart_con'),
    path('complete/<slug:orderid>/', CartComplete.as_view(), name='complete'),
]