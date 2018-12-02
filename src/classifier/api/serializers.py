from rest_framework import serializers
from classifier.models import Item, Prediction

class ItemSerializer(serializers.ModelSerializers):
    class Meta:
        model = Item
        fields = [
            'image',
            'created_at',
            'user'
        ]

class PredictionSerializer(serializers.ModelSerializers):
    class Meta:
        model = Prediction
        fields = [
            'name',
            'probability',
            'summary',
            'item'
        ]