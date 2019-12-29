from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import (
    ModelSerializer,
    CharField
)
from .models import (
    Staff
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class StaffSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = Staff
        fields = '__all__'


class StaffSerializerForList(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = Staff
        fields = [
            'email',
        ]