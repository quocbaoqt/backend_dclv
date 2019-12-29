from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import (
    ApartmentResponse,
    ApartmentResponseForList,
    ApartmentServicesResponse,
    ApartmentTypeResponse,
    ApartmentLocationResponse,
    ApartmentServicesResponseForList,
    ApartmentLocationResponseForDetail
    )


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'create/',
        ApartmentResponse.as_view({'post': 'create'}),
        name='apartment_create'
    ),
    path(
        'list/',
        ApartmentResponseForList.as_view({'get': 'list'}),
        name='apartment_create'
    ),
    path(
        'detail/<str:id>',
        ApartmentResponse.as_view({'get': 'retrieve'}),
        name='apartment_detail'
    ),
    path(
        'update/<str:id>',
        ApartmentResponse.as_view({'put': 'update'}),
        name='apartment_update'
    ),
    path(
        'delete/<str:id>',
        ApartmentResponse.as_view({'delete': 'destroy'}),
        name='apartment_delete'
    ),
    path(
        'services/create/',
        ApartmentServicesResponse.as_view({'post': 'create'}),
        name='services_create'
    ),
    path(
        'services/list/',
        ApartmentServicesResponseForList.as_view({'get': 'list'}),
        name='services_create'
    ),
    path(
        'services/detail/<str:id>',
        ApartmentServicesResponse.as_view({'get': 'retrieve'}),
        name='services_detail'
    ),
    path(
        'services/update/<str:id>',
        ApartmentServicesResponse.as_view({'put': 'update'}),
        name='services_update'
    ),
    path(
        'services/delete/<str:id>',
        ApartmentServicesResponse.as_view({'delete': 'destroy'}),
        name='services_delete'
    ),
    path(
        'location/create/',
        ApartmentLocationResponse.as_view({'post': 'create'}),
        name='location_create'
    ),
    path(
        'location/detail/<str:apartment_id>',
        ApartmentLocationResponseForDetail.as_view({'get': 'retrieve'}),
        name='location_detail'
    ),
    path(
        'type/create/',
        ApartmentTypeResponse.as_view({'post': 'create'}),
        name='type_create'
    ),

]
