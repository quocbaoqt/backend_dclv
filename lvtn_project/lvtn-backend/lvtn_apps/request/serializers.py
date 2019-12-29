from rest_framework import serializers
from rest_framework.response import Response

from .models import (
    Request
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class RequestSerializer(serializers.ModelSerializer):


    class Meta:
        model = Request
        fields = '__all__'


