from rest_framework import serializers
from .models import Item


class ItemReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id", "unique_identification_number",
            "stock_keeping_unit", "description", "weight", "size",
            "status", "metal", "price", "image_display",
        ]


class ItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "unique_identification_number",
            "stock_keeping_unit", "description", "weight", "size",
            "status", "metal", "price", "image_display",
        ]