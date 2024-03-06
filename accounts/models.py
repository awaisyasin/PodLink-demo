from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email_verification_token = models.CharField(max_length=255, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    objects = CustomUserManager()


class GuestProfile(CustomUser):
    profile_image = models.ImageField(upload_to='guest_profiles', null=True, blank=True)
    YEAR_CHOICES = [(year, str(year)) for year in range(1920, 2024)]
    year_of_birth = models.PositiveIntegerField(choices=YEAR_CHOICES)


class HostProfile(CustomUser):
    podcast_name = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='host_profiles', null=True, blank=True)
    YEAR_CHOICES = [(year, str(year)) for year in range(1920, 2024)]
    year_of_birth = models.PositiveIntegerField(choices=YEAR_CHOICES)