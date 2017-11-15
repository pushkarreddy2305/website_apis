from __future__ import unicode_literals

from django.db import models
from .member import Member
from rest_framework.exceptions import NotFound

# Create your models here.
class Item(models.Model):
    uploaded_by = models.ForeignKey(Member, null=False)
    item_name = models.CharField(max_length=200, null=True)
    item_category = models.CharField(max_length=200,default="")
    is_found = models.BooleanField(default=False)
    item_image = models.ImageField()

    def __str__(self):
        return self.item_name

    @classmethod
    def get_item_obj(cls, id):
        try:
            item_obj = cls.objects.get(id=id)
            return item_obj
        except cls.DoesNotExist:
            raise NotFound("Item not found")

    @classmethod
    def create_item(cls,item_name,item_category,uploaded_by,image):
        try:
            item_obj = cls.objects.create(
                item_name=item_name,
                item_category=item_category,
                uploaded_by = Member.objects.get(username=uploaded_by),
                item_image = image
            )
            return item_obj
        except cls.DoesNotExist:
            raise NotFound("Item not found")

    @classmethod
    def get_item_details(cls, id):
        try:
            item_obj = cls.objects.get(id=id)
            obj = {
                "image":item_obj.item_image
            }
            return obj
        except cls.DoesNotExist:
            raise NotFound("User not found")