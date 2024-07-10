from rest_framework import serializers

from services.models import *
from common.serializers import MediaURLSerializer

from clinics.serializers import SpecialistListSerializer
from clinics.models import Specialist, Diploma


class ServiceHomeListSerializer(serializers.ModelSerializer):
    gif = MediaURLSerializer()

    class Meta:
        model = Service
        fields = ('id', 'title', 'gif')


class ServiceCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'title')
        read_only_fields = fields


class ServiceListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Service
        fields = ('id', 'title', 'subtitle', 'image')
        read_only_fields = fields


class ServiceImageSerializer(serializers.Serializer):
    image = MediaURLSerializer()


class ServiceCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('title', 'value')
        read_only_fields = fields


class ProcedureCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCost
        fields = ('title', 'price')
        read_only_fields = fields


class WhoPerformsProcedureSerializer(serializers.ModelSerializer):
    specialist = SpecialistListSerializer()

    class Meta:
        model = WhoPerformsProcedure
        fields = ('id', 'specialist')
        read_only_fields = fields


class ServiceDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    images = ServiceImageSerializer(many=True)
    characteristics = ServiceCharacteristicSerializer(many=True)
    procedure_costs = ProcedureCostSerializer(many=True)
    who_performs_procedures = WhoPerformsProcedureSerializer(many=True)

    class Meta:
        model = Service
        fields = ('id', 'title', 'subtitle', 'image', 'for_what',
                  'short_desc', 'desc', 'price', 'category', 'images',
                  'characteristics', 'procedure_costs',
                  'who_performs_procedures')
        read_only_fields = fields


class DiplomaSerializer(serializers.ModelSerializer):
    file = MediaURLSerializer()

    class Meta:
        model = Diploma
        fields = ('file',)


class SpecialistProcedureSerializer(serializers.ModelSerializer):
    service = ServiceListSerializer()

    class Meta:
        model = WhoPerformsProcedure
        fields = ('id', 'service')
        read_only_fields = fields


class SpecialistDetailSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()
    diplomas = DiplomaSerializer(many=True)
    procedures = SpecialistProcedureSerializer(many=True)

    class Meta:
        model = Specialist
        fields = ('id', 'full_name', 'position', 'about', 'certificates',
                  'photo', 'experience_in_company', 'experience_in_field',
                  'experience_in_years',
                  'diplomas', 'procedures')

        read_only_fields = fields


class OrderServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderService
        fields = ('phone', 'full_name', 'book_date', 'service')
