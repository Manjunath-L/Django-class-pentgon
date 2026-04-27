from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", 'name', 'description', 'price', 'stock', 'image')

    def validate(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
