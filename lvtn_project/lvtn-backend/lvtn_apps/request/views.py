from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q

from .models import (
    Request,
)
from .serializers import (
    RequestSerializer,
    # UserRegisterSerializer,
    # RegisterUserPhoneOnlySerializer,
    # UpdateUserProfileSerializer,
    # UpdateUserAvatarSerializer,
    # UserSettingValueSerializer,
    # UserSettingValueSerializerForList,
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class RequestResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    # def list(self, request, *args, **kwargs):
    #     try:
    #         response_data = super().list(request, *args, **kwargs)
    #         self.response_format["data"] = response_data.data
    #     except Exception as e:
    #         self.response_format["message"] = str(e)
    #         self.response_format["errorCode"] = 500
    #     return Response(self.response_format)
    def perform_create(self, serializer):   
        if(self.request.data.get('send_all')=='true'):
            serializer.save(receiver=None)
        else:
            serializer.save()

    def create(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        try:
            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

    # def retrieve(self, request, *args, **kwargs):
    #     try:
    #         response_data = super().retrieve(request, *args, **kwargs)
    #         self.response_format["data"] = response_data.data
    #     except Exception as e:
    #         self.response_format["message"] = str(e)
    #         self.response_format["errorCode"] = 500
    #     return Response(self.response_format)


class RequestResponseForList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def get_queryset(self):
        queryset = Message.objects.filter(Q(receiver=self.request.user) | Q(receiver=None))
        # import pdb; pdb.set_trace()
        return queryset
    
    def list(self, request, *args, **kwargs):
        try:
            response_data = super().list(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)
