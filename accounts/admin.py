from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.HostProfile)
admin.site.register(models.GuestProfile)