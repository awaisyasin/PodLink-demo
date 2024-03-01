from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models

# Create your forms here.

class GuestSignUpForm(UserCreationForm):
    class Meta:
        model = models.GuestProfile
        fields = ['first_name', 'last_name', 'year_of_birth', 'email', 'password1', 'password2']


class HostSignUpForm(UserCreationForm):
    class Meta:
        model = models.HostProfile
        fields = ['first_name', 'last_name', 'year_of_birth', 'email', 'podcast_name', 'password1', 'password2']