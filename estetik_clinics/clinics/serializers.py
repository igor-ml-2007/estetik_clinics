from rest_framework import serializers

from clinics.models import *
from common.serializers import MediaURLSerializer
from products.serializers import ProductListSerializer

class SpecialistListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    position = serializers.CharField()
    photo = MediaURLSerializer()
    experience_in_years = serializers.IntegerField()


class OnlineAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineAppointment
        fields = ('phone_number', 'full_name', 'book_date')


class VacancyListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'image', 'responsibilities',
                  'requirements', 'conditions')


class ActionImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ActionImage
        fields = ('id', 'image')
        read_only_fields = fields


class ActionListSerializer(serializers.ModelSerializer):
    action_images = ActionImageSerializer(many=True)

    class Meta:
        model = Action
        fields = ('id', 'title', 'special_offer', 'short_desc',
                  'in_discount', 'percentage', 'expires_in',
                  'action_images', 'desc')
        read_only_fields = fields


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'title')
        read_only_fields = fields


class NewsListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = News
        fields = ('id', 'title', 'image', 'desc', 'created_at', 'special_offer')
        read_only_fields = fields


class NewsDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    category = serializers.CharField(source='category.title')
    tags = serializers.ListSerializer(child=serializers.CharField(source='tag.title'))

    class Meta:
        model = News
        fields = ('title', 'image', 'desc', 'category', 'created_at', 'special_offer',
                  'tags', 'category')
        read_only_fields = fields


class ContactChiefDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactChiefDoctor
        fields = ('phone_number', 'full_name', 'message')
        write_only_fields = fields


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('full_name', 'phone_number', 'text')
        write_only_fields = fields


class FeedbackListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Feedback
        fields = ('full_name', 'created_at', 'text', 'image')
        read_only_fields = fields

class AboutUsSerializer(serializers.Serializer):
    video = MediaURLSerializer()
    summary = serializers.CharField()

class PhotoGalleryCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class PhotoGallerySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    photo = MediaURLSerializer()

class LicenseSerializer(serializers.ModelSerializer):
    photo = MediaURLSerializer()

    class Meta:
        model = License
        fields = ('id', 'title', 'photo')
        read_only_fields = fields

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"
        read_only_fields = [fields]

class HomeSliderSerializer(serializers.ModelSerializer):
    file = MediaURLSerializer()

    class Meta:
        model = HomeSlider
        fields = ('id', 'file', 'title', 'desc')
        read_only_fields = fields


class StoryCategoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = StoryCategory
        fields = ('id', 'title', 'image')
        read_only_fields = fields

class StoryProductListSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()

    class Meta:
        model = StoryProduct
        fields = ('item', )

    def get_item(self, obj):
        return ProductListSerializer(obj.product).data

class StoryListSerializer(serializers.ModelSerializer):
    video = MediaURLSerializer()
    products = None

    class Meta:
        model = Story
        fields = ('id', 'title', 'video')


class StoryCategoryDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    stories = StoryListSerializer(many=True)

    class Meta:
        model = StoryCategory
        fields = ('id', 'title', 'image')