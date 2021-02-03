from rest_framework import serializers
from .models import RecipeMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeMerch
        fields = ('id','name', 'description', 'price')
