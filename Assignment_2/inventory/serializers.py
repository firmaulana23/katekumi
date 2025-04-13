from rest_framework import serializers
from .models import Item, Purchase, Sell

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class StockReportSerializer(serializers.Serializer):
    item_code = serializers.CharField()
    name = serializers.CharField()
    unit = serializers.CharField()
    stock_changes = serializers.ListField(child=serializers.DictField())