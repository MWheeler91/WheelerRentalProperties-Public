from rest_framework import serializers
from .models import *


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    fullAddress = serializers.ReadOnlyField(source='full_address')
    short_address = serializers.ReadOnlyField(source='address')
    class Meta:
        model = Property
        fields = '__all__'


class PropertyImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id',
            'full_address',
            'address',
            'rent',
            'bedrooms',
            'bathrooms',
            'sq_foot',
            'available_date',
            'slug',
            'is_active',
            'description'
        ]
#
#
# class PropertyDetailsSerializer(serializers.ModelSerializer):
#     property_details_extended = PropertyDetails_ExtendedSerializer(many=True)
#
#     class Meta:
#         model = Property
#         fields = '__all__'
