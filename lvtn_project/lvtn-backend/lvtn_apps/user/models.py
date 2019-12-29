import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
import datetime
# from leaveform_apps.user.models import User

class UserManager(AbstractBaseUser):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,department,email,password=None):
        return self._create_user(email,password,department=department)
    def create_superuser(self,department,email,password=None):
        return self._create_user(
            email,password,department=department,is_staff=True,
            is_supperuser=True
        )

class User(AbstractBaseUser):
    
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)

    last_login = None #important
    is_staff = None
    first_name = models.CharField(max_length=100,default = "")
    last_name = models.CharField(max_length=100,default = "")
    city = models.CharField(max_length=100,default = "")
    district = models.CharField(max_length=100,default = "")
    street = models.CharField(max_length=100,default = "")
    birthday = models.DateField(null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['department','city','district','street']

    objects = UserManager()

    def __str__(self):
        return self.email

