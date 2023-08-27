from rest_framework import serializers
from .models import *

class BaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bale
        fields = ['clothe_type', 'material', 'origin_country', 'weight', 'age', 'gender', 'season', 'grade', 'code','pieces','price','created']

    
    def create(self, validated_data):

        return Bale.objects.create(**validated_data)
    
# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ['store_name', 'bale_origin', 'store_owner', 'bale_weight']