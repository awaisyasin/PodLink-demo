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


class HostSignUpForm(UserCreationForm):
    class Meta:
        model = models.HostProfile
        fields = ['first_name', 'last_name', 'year_of_birth', 'email', 'podcast_name', 'password1', 'password2']


UserModel = get_user_model()

class CustomAutenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"autofocus": True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise forms.ValidationError('Invalid email')

        if not user.check_password(password):
            raise forms.ValidationError('Invalid password')

        if not user.is_active:
            raise forms.ValidationError('This account is inactive')

        return self.cleaned_data

    def get_user(self):
        email = self.cleaned_data['email']

        if email:
            try:
                user = UserModel.objects.get(email=email)
                return user
            except UserModel.DoesNotExist:
                return None
        return None