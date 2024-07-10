from rest_framework import serializers


class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, media):
        if not media:
            return None
        # Постараемся получить абсолютный URL-адрес файла
        try:
            return self.context["request"].build_absolute_uri(media.file.url)
        except Exception:
            return "http://testserver" + str(media.file.url)


class ConfigSerializer(serializers.Serializer):
    main_phone_number = serializers.CharField(max_length=20)
    our_clinic_text = serializers.CharField()
    service_page_back_image = MediaURLSerializer()
    product_page_back_image = MediaURLSerializer()
    vacancy_page_back_image = MediaURLSerializer()
    contact_page_back_image = MediaURLSerializer()
