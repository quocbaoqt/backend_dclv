from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    Message
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = '__all__'
