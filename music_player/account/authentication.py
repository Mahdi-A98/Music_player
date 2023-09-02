from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from .models import User
from django.db.models import Q

class MyUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        username=username
        password=password
        try:
            user= User.objects.get(Q(email=username) | Q(username=username))
            if user:
                if user.check_password(password):
                    return user
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
