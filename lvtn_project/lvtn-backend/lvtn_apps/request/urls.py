from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import (
    RequestResponse,
    RequestResponseForList
    # GetUserProfileResponse,
    # UpdateUserProfileResponse,
)


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'create/',
        RequestResponse.as_view({'post': 'create'}),
        name='request_create'
    ),
    path(
        'list/',
        RequestResponseForList.as_view({'get': 'list'}),
        name='request_list'
    ),
    path(
        'detail/<str:id>',
        RequestResponse.as_view({'get': 'retrieve'}),
        name='request_detail'
    ),
]
