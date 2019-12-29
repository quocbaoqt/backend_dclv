import os
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# from leaveform_apps.user.models import User


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=20, unique=True)
    email = models.EmailField(_('email address'), null=True)
    phone_number = models.CharField(
        _('Phone Number'),
        unique=True,
        max_length=20
    )


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return "{}".format(self.username)



class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    dob = models.DateField(blank=True, null=True)
    email = models.EmailField(_('email address'), blank=False)
    # avatar = models.FileField(
    #     # upload_to='user/',
    #     upload_to=generate_name_image,
    #     null=True,
    #     blank=True,
    #     validators=[
    #         FileExtensionValidator(
    #             allowed_extensions=['png', 'jpeg', 'jpg', 'svg']
    #             )
    #         ]
    #     )

    user_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=255)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return '{}'.format(self.user_name)
    # def __str__(self):
    #     return self.pk
