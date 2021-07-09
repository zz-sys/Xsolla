from rest_framework import serializers, viewsets
from XsollaAPI.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockUnit
        fields = '__all__'
        depth = 1


class UnitAtStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitAtStorage
        fields = '__all__'
        depth = 2
