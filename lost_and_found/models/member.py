from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from rest_framework.exceptions import NotFound, ParseError, AuthenticationFailed
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    username = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.username

    @classmethod
    def sign_up(cls, request_data):
        from lost_and_found.utils.utility_functions import check_username_present
        check_username_present(request_data.username)

        try:
            from django.db import transaction
            with transaction.atomic():
                from django.contrib.auth.models import User
                user_obj = User.objects.create_user(username=request_data.username,
                                               password=request_data.password)
                print(user_obj)
                member_obj = cls.objects.create(
                    user_id=user_obj.id,
                    username=request_data.username,
                    email=request_data.email,
                    first_name=request_data.first_name,
                    last_name=request_data.last_name,
                    city=request_data.city
                )
                print("again")
                return member_obj
        except Exception as x:
            print(x)
            raise ParseError("Member cannot be registered")


    @classmethod
    def login(cls, request_obj):
        try:
            user = User.objects.get(username=request_obj.username)
            if user.check_password(request_obj.password):
                user = user
                return cls.objects.get(user=user)
        except User.DoesNotExist:
            raise AuthenticationFailed("Username or password is incorrect")

    @classmethod
    def get_member_obj(cls, username):
        try:
            member_obj = cls.objects.get(username=username)
            return member_obj
        except cls.DoesNotExist:
            raise NotFound("User not found")

    @classmethod
    def get_member_details_by_id(cls, id):
        try:
            member_obj = cls.objects.get(id=id)
            obj = {
                "username": member_obj.username,
                "first_name": member_obj.first_name,
                "last_name": member_obj.last_name,
                "city": member_obj.city,
                "email": member_obj.email,
            }
            return obj
        except cls.DoesNotExist:
            raise NotFound("User not found")

    @classmethod
    def get_member_details_by_username(cls, username):
        try:
            member_obj = cls.objects.get(username=username)
            obj = {
                "username": member_obj.username,
                "first_name": member_obj.first_name,
                "last_name": member_obj.last_name,
                "city": member_obj.city,
                "email": member_obj.email,
            }
            return obj
        except cls.DoesNotExist:
            raise NotFound("User not found")

    @classmethod
    def update_profile(cls, request_data):
        try:
            from django.db import transaction
            with transaction.atomic():

                from django.contrib.auth.models import User
                user_obj = User.objects.get(username=request_data.username)
                user_obj.set_password(request_data.password)
                user_obj.save()
                member_obj = cls.objects.get(user=user_obj)
                if member_obj.username != request_data.username:
                    from lost_and_found.utils.utility_functions import check_username_present
                    check_username_present(request_data.username)
                member_obj.user = user_obj
                member_obj.username = request_data.username
                member_obj.email = request_data.email
                member_obj.first_name = request_data.first_name
                member_obj.last_name = request_data.last_name
                member_obj.city = request_data.city
                member_obj.save()
                return member_obj
        except:
            raise ParseError("Student Profile cannot be Updated")
