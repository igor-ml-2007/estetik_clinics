from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from services.serializers import *


class ServiceHomeListView(ListAPIView):
    queryset = Service.objects.filter(is_home_page=True)
    serializer_class = ServiceHomeListSerializer


class ServiceCategoryListAPIView(ListAPIView):
    queryset = ServiceCategory.objects.filter(parent__isnull=True)
    serializer_class = ServiceCategoryListSerializer


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer


class OrderServiceAPIView(CreateAPIView):
    queryset = OrderService.objects.all()
    serializer_class = OrderServiceSerializer


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    # TODO: Создать view для сортировки по категориям сервисов

