from rest_framework import serializers
from . import models

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Item
        fields = ('id', 'itemname', 'itemdescription', 'itemOwner',)
        read_only_fields = ('id',)

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Seller
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Buyer
        fields = ('id', 'username', 'password', )
        read_only_fields = ('id',)