from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import (
    ModelSerializer,
    CharField
)
from .models import (
    User
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = '__all__'


class UserSerializerForList(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = [
            'user_name',
            'email',
        ]