from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    User,
    UserProfile
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializerForList(serializers.ModelSerializer):
    # profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone_number'
        ]

class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        # user.is_staff = True
        # Allow user login to the system.
        # Just a temp solution to allow generating token for this user.
        user.save()
        return user