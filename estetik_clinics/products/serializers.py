from rest_framework import serializers

from products.models import *
from common.serializers import MediaURLSerializer



class ProductImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductImage
        exclude = ['product']
        read_only_fields = ['id', 'image']

class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    manufacturer = serializers.CharField(source='manufacturer.name')
    price = serializers.FloatField()
    product_images = ProductImageSerializer(many=True)

class CharacteristicsValueSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class CharacteristicsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    values = CharacteristicsValueSerializer(many=True)

class InstructionSerializer(serializers.ModelSerializer):
    right_image = MediaURLSerializer()
    left_image = MediaURLSerializer()

    class Meta:
        model = Instruction
        exclude = ['product']

class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    product_images = ProductImageSerializer(many=True)
    characteristics = CharacteristicsSerializer(many=True)
    instructions = InstructionSerializer(many=True)
    recommended_products = serializers.SerializerMethodField()


    class Meta:
        model = Product
        exclude = ['view_count', 'manufacturer', 'created_at']
        read_only_fields = ['id', 'title', 'description', 'discount', 'price', 'product_images',
                            'category', 'short_desc', 'recommended_products']

    def get_recommended_products(self, obj):
        recommended_products = Product.objects.filter(category_id=obj.category_id).exclude(id=obj.id)[:8]
        return ProductListSerializer(recommended_products, many=True)


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'products')


class ManufacturerListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj):
        return obj.product_set.count()


class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'title', 'products_count')

    def get_products_count(self, obj):
        return obj.product_set.count()