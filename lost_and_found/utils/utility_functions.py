from rest_framework.exceptions import PermissionDenied


def check_username_present(username):
    from django.contrib.auth.models import User
    user = User.objects.filter(username=username)
    if user.count() != 0:
        raise PermissionDenied("username already exists")