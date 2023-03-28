from django.urls import path
from .views import HomePageView, ProductView

urlpatterns = [
    path('',HomePageView.as_view(),name = 'home'),
    path('product/<int:pk>',ProductView.as_view(),name='product'),
]