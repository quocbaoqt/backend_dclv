from django.urls import include
from django.urls import path
from rest_framework import routers
from .views import (
    MessageResponse
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
]
