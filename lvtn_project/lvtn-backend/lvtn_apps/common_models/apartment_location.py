from django.db import models

from ..apartment.models import Apartment
# HCM = 'hcm'
# HN = 'hn'

# CITY = [
#     (HCM, 'Hồ Chí Minh'),
#     (HN, 'Hà Nội'),
# ]

# DISTRICT = [
#     (HCM, 'Hồ Chí Minh'),
#     (HN, 'Hà Nội'),
# ]


class ApartmentLocation(models.Model):
    apartment = models.ForeignKey(
        Apartment,
        to_field="id",
        db_column="apartment_id",
        related_name="apartment_location",
        on_delete=models.CASCADE,
    )
    # V1: using textfield
    # city = models.CharField(
    #     max_length=50,
    #     choices=CITY,
    #     default=HCM,
    #     unique=True,
    # )
    # district = models.CharField(
    #     max_length=50,
    #     choices=DISTRICT,
    #     default=Q1,
    #     unique=True,
    # )
    city = models.TextField()
    district = models.TextField()
    address = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title