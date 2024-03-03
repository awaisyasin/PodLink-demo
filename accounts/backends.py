from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, username=None, password=None, **kwargs):
        if (email is None and username is None) or password is None:
            return None

        UserModel = get_user_model()

        if email is not None:
            try:
                user = UserModel.objects.get(email=email)
            except UserModel.DoesNotExist:
                return None
        else:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None
