from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    Apartment,
    ApartmentServices
)
from ..common_models.apartment_type import ApartmentType
from ..common_models.apartment_location import ApartmentLocation
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class ApartmentSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentSerializerForList(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)
    # city = serializers.SerializerMethodField()
    # district = serializers.SerializerMethodField()
    # address = serializers.SerializerMethodField()


    # def city(self, obj):
    #     import pdb; pdb.set_trace()
    #     return obj.get_type_product_display()
    # def district(self, obj):
    #     return obj.get_type_product_display()
    # def address(self, obj):
    #     return obj.get_type_product_display()

    class Meta:
        model = Apartment
        fields = [
            'id',
            'title',
            'apartment_type',
            'price',
            'status',
            'cover',
            'city',
            'district',
            'address',
        ]


class ApartmentServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApartmentServices
        fields = '__all__'

class ApartmentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApartmentType
        fields = '__all__'


class ApartmentLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApartmentLocation
        fields = '__all__'
