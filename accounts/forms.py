from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from . import models

# Create your forms here.

class GuestSignUpForm(UserCreationForm):
    class Meta:
        model = models.GuestProfile
        fields = ['first_name', 'last_name', 'year_of_birth', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.required = True


class HostSignUpForm(UserCreationForm):
    class Meta:
        model = models.HostProfile
        fields = ['first_name', 'last_name', 'year_of_birth', 'email', 'podcast_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.required = True


UserModel = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"autofocus": True}))

    class Meta:
        fields = ['email', 'password']

    # field_order = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def get_user(self):
        email = self.cleaned_data['email']

        if email:
            try:
                user = UserModel.objects.get(email=email)
                return user
            except UserModel.DoesNotExist:
                return None
        return None