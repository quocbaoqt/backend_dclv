"""lvtn_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.documentation import include_docs_urls

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_swagger_view(title='LVTN API')
urlpatterns = [
    path('', schema_view),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('docs/', include_docs_urls(title='API Lvtn')),
    path('admin/', admin.site.urls),
    path('accounts/login/', schema_view),
    path('user/', include('lvtn_apps.user.urls')),
    path('apartment/', include('lvtn_apps.apartment.urls')),
    path('message/',include('lvtn_apps.message.urls')),
    path('request/',include('lvtn_apps.request.urls')),
    # path('auth/', include('lvtn_apps.user.urls')),
    # path('leaveform/', include('leaveform_apps.leave_form.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
