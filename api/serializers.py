from rest_framework import serializers

from .models import NFT, Collection


class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
