from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from .models import Token

UserModel = get_user_model()


class UrlTokenBackend(ModelBackend):
    def authenticate(self, token):
        try:
            user = Token.objects.get(token=token).user
        except Token.DoesNotExist:
            return None

        if not user.is_active:
            return None

        return user

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
