from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import (
    UserResponse,
    UserResponseForList,
    UserRegisterResponse
    # GetUserProfileResponse,
    # UpdateUserProfileResponse,
)

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'register/',
        UserRegisterResponse.as_view({'post': 'create'}),
        name='user_create'
    ),
    path(
        'list/',
        UserResponseForList.as_view({'get': 'list'}),
        name='user_list'
    ),
    path(
        'detail/<str:id>',
        UserResponse.as_view({'get': 'retrieve'}),
        name='user_detail'
    ),
    path(
        'update/<str:id>',
        UserResponse.as_view({'put': 'update'}),
        name='user_update'
    ),
    path(
        'delete/<str:id>',
        UserResponse.as_view({'delete': 'destroy'}),
        name='user_delete'
    ),
]
