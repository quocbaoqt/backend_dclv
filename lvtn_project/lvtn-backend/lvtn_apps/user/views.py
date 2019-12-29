from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import (
    User,
    UserProfile
)
from .serializers import (
    UserSerializer,
    UserSerializerForList,
    UserRegisterSerializer,
    # UserRegisterSerializer,
    # RegisterUserPhoneOnlySerializer,
    # UpdateUserProfileSerializer,
    # UpdateUserAvatarSerializer,
    # UserSettingValueSerializer,
    # UserSettingValueSerializerForList,
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class UserResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
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


class UserResponseForList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAdminUser
    ]
    serializer_class = UserSerializerForList
    queryset = User.objects.all()

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



class UserRegisterResponse(viewsets.ModelViewSet):
    """
        Following class is for register new account with username.
        Does not require any additional field.
    """
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def check_username(self, request, *args, **kwargs):
        response_format = self.response_format
        response_format["data"] = {"existing": False}
        if User.objects.filter(username=kwargs['username']).exists():
                response_format["data"] = {"existing": True}
                response_format["message"] = kwargs['username'] + ' is already existed.'
        return Response(response_format)

    def create(self, request, *args, **kwargs):
        try:
            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as exc:
            self.response_format["message"] = str(exc)
            self.response_format["errorCode"] = 500

        return Response(self.response_format)


class GetUserProfileResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated  # Need to allow current logged in user update it's profiles only
    ]
    serializer_class = UserSerializer

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(GetUserProfileResponse, self).__init__(**kwargs)

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

    # def retrieve_manually(self, request, *args, **kwargs):
    #     serialiser = UserSerializer(request.user)
    #     self.response_format["data"] = serialiser.data
    #     return Response(self.response_format)

    def retrieve(self, request, *args, **kwargs):
        response_data = super(
            GetUserProfileResponse,
            self
            ).retrieve(request, *args, **kwargs)
        self.response_format["data"] = response_data.data
        return Response(self.response_format)