from django.urls import path
from services.views import *

urlpatterns = [
    path('', ServiceListAPIView.as_view(), name='services'),
    path('home-services/', ServiceHomeListView.as_view(), name='home-services'),
    path('categories/', ServiceCategoryListAPIView.as_view(), name='service-categories'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('order_service/', OrderServiceAPIView.as_view(), name='order-service')
]
