from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import (
    MessageResponse,
    MessageResponseForList
    # GetUserProfileResponse,
    # UpdateUserProfileResponse,
)


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'create/',
        MessageResponse.as_view({'post': 'create'}),
        name='message_create'
    ),
    path(
        'list/',
        MessageResponseForList.as_view({'get': 'list'}),
        name='message_list'
    ),
    path(
        'detail/<str:id>',
        MessageResponse.as_view({'get': 'retrieve'}),
        name='message_detail'
    ),
]
