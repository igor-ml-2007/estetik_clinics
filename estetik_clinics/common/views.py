from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from common.serializers import *
from common.models import *



class ConfigView(RetrieveAPIView):
    serializer_class = ConfigSerializer
    queryset = CommonSettings.objects.all()

    def get_object(self):
        return CommonSettings.objects.first()

