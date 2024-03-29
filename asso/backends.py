from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return None

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
