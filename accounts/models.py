from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.

class GuestProfile(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True)
    YEAR_CHOICES = [
        (year, str(year)) for year in range(1920, 2024)
    ]
    year_of_birth = models.PositiveIntegerField(choices=YEAR_CHOICES)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="guest_set",
        related_query_name="guest",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="guest_set",
        related_query_name="guest",
    )


class HostProfile(AbstractUser):
    profile_image = models.ImageField(null=True, blank=True)
    YEAR_CHOICES = [
        (year, str(year)) for year in range(1920, 2024)
    ]
    year_of_birth = models.PositiveIntegerField(choices=YEAR_CHOICES)
    podcast_name = models.CharField(max_length=255)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="host_profiles",
        related_query_name="host",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="guest_profiles",
        related_query_name="host",
    )