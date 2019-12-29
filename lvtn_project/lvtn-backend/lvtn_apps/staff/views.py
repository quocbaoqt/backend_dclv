from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .models import (
    Staff,
)
from .serializers import (
    StaffSerializer,
    StaffSerializerForList,
    # StaffRegisterSerializer,
    # RegisterStaffPhoneOnlySerializer,
    # UpdateStaffProfileSerializer,
    # UpdateStaffAvatarSerializer,
    # StaffSettingValueSerializer,
    # StaffSettingValueSerializerForList,
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class StaffResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        try:
            response_data = super().list(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

    def create(self, request, *args, **kwargs):
        try:
            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

    def retrieve(self, request, *args, **kwargs):
        try:
            response_data = super().retrieve(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

    def update(self, request, *args, **kwargs):
        try:
            response_data = super().update(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

    def destroy(self, request, *args, **kwargs):
        try:
            response_data = super().destroy(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)


class StaffResponseForList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = StaffSerializerForList
    queryset = Staff.objects.all()

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def list(self, request, *args, **kwargs):
        try:
            response_data = super().list(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)