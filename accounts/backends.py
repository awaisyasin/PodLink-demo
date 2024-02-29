from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        UserModel = get_user_model()

        if not UserModel:
            return None

        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
