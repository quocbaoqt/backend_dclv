from django.db import models


STUDIO = 'studio'
DUPLEXHOUSE = 'duplex_house'
APARTMENT = 'apartment'

APARTMENT_TYPE = [
    (STUDIO, 'Studio'),
    (DUPLEXHOUSE, 'Duplex House'),
    (APARTMENT, 'Apartment'),
]


class ApartmentType(models.Model):
    type = models.CharField(
        max_length=50,
        choices=APARTMENT_TYPE,
        default=STUDIO,
        unique=True,
    )
    # type = models.TextField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.type
