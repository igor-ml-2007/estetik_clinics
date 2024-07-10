from products.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.only('id', 'title', 'short_desc', 'price').order_by('-created_at')
    serializer_class = ProductListSerializer


    #TODO: Parameter is_in_home

class ProductFilterListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer

class ManufacturerListAPIView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer