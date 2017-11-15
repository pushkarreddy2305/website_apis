from rest_framework import serializers


class ItemType(object):
    def __init__(self, item_name, item_category, uploaded_by, item_image,id, **kwargs):
        self.item_name = item_name
        self.item_category = item_category
        self.uploaded_by = uploaded_by
        self.item_image = item_image
        self.id =id

    def __unicode__(self):
        return str(self)


    def __getitem__(self, item):
        return getattr(self, item)


class ItemSerializer(serializers.Serializer):
    item_name = serializers.CharField()
    item_category = serializers.CharField()
    uploaded_by = serializers.CharField()
    item_image = serializers.FileField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return ItemType(**validated_data)
