import uuid
from decimal import Decimal
# from django.utils import timezone

from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)
from django.contrib.postgres.fields import ArrayField

from lvtn_apps.user.models import User
# from ..common_models.apartment_location import ApartmentLocation
from lvtn_apps.utils.method_utils import generate_name_image



class Message(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    send_all = models.BooleanField(default=True)
    receiver = models.ForeignKey(
        User,
        to_field="id",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='receiver',
    )
    file = models.FileField(
        upload_to=generate_name_image,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.pk
