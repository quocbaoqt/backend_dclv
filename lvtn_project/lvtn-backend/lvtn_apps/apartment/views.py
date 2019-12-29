import json

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
    Apartment,
    ApartmentServices,
)
from ..common_models.apartment_location import ApartmentLocation
from ..common_models.apartment_type import ApartmentType

from .serializers import (
    ApartmentSerializer,
    ApartmentSerializerForList,
    ApartmentServicesSerializer,
    ApartmentTypeSerializer,
    ApartmentLocationSerializer,

    # UserRegisterSerializer,
    # RegisterUserPhoneOnlySerializer,
    # UpdateUserProfileSerializer,
    # UpdateUserAvatarSerializer,
    # UserSettingValueSerializer,
    # UserSettingValueSerializerForList,
)
# from ims_apps.common_models.ResponseInfo import ResponseInfo
from ..common_models.ResponseInfo import ResponseInfo


class ApartmentResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def perform_create(self, serializer):
        self.response_data_id = serializer.save()

    def create(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        try:
            request.data._mutable = True
            city = request.data.get('city')
            district = request.data.get('district')
            address = request.data.get('address') 
            notes = request.data.get('notes')
            services = json.loads(request.data.get('services'))
            request.data.pop('services')
            request.data._mutable = False
            # import pdb; pdb.set_trace()

            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
            for service in services:
                service = ApartmentServices.objects.create(
                    title=service.get('title'),
                    cost=service.get('cost'),
                    apartment=self.response_data_id
                )
                service.save()
            # import pdb; pdb.set_trace()
            apartment_location = ApartmentLocation.objects.create(
                address=address,
                city=city,
                district=district,
                notes=notes,
                apartment=self.response_data_id
            )
            apartment_location.save()


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


class ApartmentResponseForList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApartmentSerializerForList
    queryset = Apartment.objects.all()

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


class ApartmentServicesResponseForList(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentServicesSerializer
    queryset = ApartmentServices.objects.all()
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)
    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(apartment = self.request.query_params.get('id'))
    def list(self, request, *args, **kwargs):
        try:
            response_data = super().list(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)

class ApartmentServicesResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentServicesSerializer
    queryset = ApartmentServices.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

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


class ApartmentTypeResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentTypeSerializer
    queryset = ApartmentType.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def create(self, request, *args, **kwargs):
        try:
            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)


class ApartmentLocationResponse(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentLocationSerializer
    queryset = ApartmentLocation.objects.all()
    lookup_field = 'id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def create(self, request, *args, **kwargs):
        try:
            response_data = super().create(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)


class ApartmentLocationResponseForDetail(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny  
    ]
    serializer_class = ApartmentLocationSerializer
    queryset = ApartmentLocation.objects.all()
    lookup_field = 'apartment_id'

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super().__init__(**kwargs)

    def retrieve(self, request, *args, **kwargs):
        try:
            response_data = super().retrieve(request, *args, **kwargs)
            self.response_format["data"] = response_data.data
        except Exception as e:
            self.response_format["message"] = str(e)
            self.response_format["errorCode"] = 500
        return Response(self.response_format)