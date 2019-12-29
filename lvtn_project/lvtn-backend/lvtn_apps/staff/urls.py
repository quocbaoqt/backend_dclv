from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import (
    StaffResponse,
    StaffResponseForList,
    # GetStaffProfileResponse,
    # UpdateStaffProfileResponse,
)


router = routers.DefaultRouter()
# router.register(r'Staffs', StaffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'create/',
        StaffResponse.as_view({'post': 'create'}),
        name='Staff_create'
    ),
    path(
        'list/',
        StaffResponseForList.as_view({'get': 'list'}),
        name='Staff_list'
    ),
    path(
        'detail/<str:id>',
        StaffResponse.as_view({'get': 'retrieve'}),
        name='Staff_detail'
    ),
    path(
        'update/<str:id>',
        StaffResponse.as_view({'put': 'update'}),
        name='Staff_update'
    ),
    path(
        'delete/<str:id>',
        StaffResponse.as_view({'delete': 'destroy'}),
        name='Staff_delete'
    ),
]
