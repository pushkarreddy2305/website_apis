from django.contrib import admin
from .models.member import Member
from .models.item import Item

admin.site.register(Member)
admin.site.register(Item)
# Register your models here.
