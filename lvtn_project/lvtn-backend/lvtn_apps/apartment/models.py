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

from ..common_models.apartment_type import ApartmentType
from lvtn_apps.utils.method_utils import generate_name_image
# from ..common_models.apartment_location import ApartmentLocation



zero = '0'
one = '1'
two = '2'
three = '3'

ROOMS = [
    (zero, '0'),
    (one, '1'),
    (two, '2'),
    (three, '3')
]


class Apartment(models.Model):
    title = models.CharField(max_length=100)
    apartment_type = models.ForeignKey(
        ApartmentType,
        to_field="type",
        on_delete=models.CASCADE,
        related_name='apartment_type',
    )
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0'),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(999999999999)
        ],
    )
    status = models.TextField()
    # location = models.ForeignKey(
    #     ApartmentLocation,
    #     to_field="id",
    #     db_column="apartment_location",
    #     on_delete=models.CASCADE,
    #     related_name='apartment_location',
    # )
    city = models.TextField()
    district = models.TextField()
    address = models.TextField()
    notes = models.TextField()
    # services = models.ForeignKey(
    #     ApartmentServices,
    #     to_field="id",
    #     db_column="apartment_services",
    #     on_delete=models.CASCADE,
    #     related_name='apartment_services',
    # )


    # rooms 
    living_rooms = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )
    dinning_rooms = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )
    bed_rooms = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )
    bath_rooms = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )
    toilets = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )
    kitchen = models.CharField(
        max_length=50,
        choices=ROOMS,
        default=zero,
    )

    furnitures = ArrayField(models.CharField(max_length=100), blank=True, size=12)

    description = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image_1 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_2 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_3 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_4 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_5 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_6 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_7 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    image_8 = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    cover = models.FileField(
        upload_to=generate_name_image,
        # upload_to='product/',

        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
                )
            ]
        )
    def __str__(self):
        return self.pk


class ApartmentServices(models.Model):
    title = models.CharField(max_length=100)
    apartment = models.ForeignKey(
        Apartment,
        to_field="id",
        db_column="apartment_id",
        on_delete=models.CASCADE,
        related_name='apartment_services',
    )
    cost = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(999999999999)
        ],
    )

    # def __str__(self):
        # return self.title