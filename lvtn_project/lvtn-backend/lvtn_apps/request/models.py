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
from lvtn_apps.apartment.models import Apartment
# from ..common_models.apartment_location import ApartmentLocation
from lvtn_apps.utils.method_utils import generate_name_image



pending = 'pending'
processing = 'processing'
cancel = 'cancel'
done = 'done'

STATUS = [
    (pending, 'pending'),
    (processing, 'processing'),
    (cancel, 'cancel'),
    (done, 'done')
]


class Request(models.Model):
    title = models.CharField(max_length=100)
    started_date = models.DateField()
    ended_date = models.DateField()
    user_request = models.ForeignKey(
        User,
        to_field="id",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='user_request',
    )
    apartment_request = models.ForeignKey(
        Apartment,
        to_field="id",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='apartment_request',
    )
    
    type =  models.CharField(
        max_length=50,
        choices=STATUS,
        default='pending',
    )
    description = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.pk