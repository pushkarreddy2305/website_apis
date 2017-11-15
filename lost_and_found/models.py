from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name
