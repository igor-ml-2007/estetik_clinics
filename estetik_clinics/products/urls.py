from django.urls import path
from products.views import *


urlpatterns = [
    path('home/', ProductListAPIView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/', CreateOrderAPIView.as_view(), name='order'),
    path('manufacturer/', ManufacturerListAPIView.as_view(), name='manufacturer'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('', ProductFilterListAPIView.as_view(), name='product-filter')
]