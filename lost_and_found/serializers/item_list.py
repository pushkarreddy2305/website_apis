from rest_framework import serializers

from lost_and_found.utils.deserialize import deserialize


class ItemListResponseType(object):
    def __init__(self, total=None, items=None, **kwargs):
        self.total = total
        self.items = items

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ItemListResponseSerializer(serializers.Serializer):
    from lost_and_found.serializers.item import ItemSerializer
    items = ItemSerializer(required=False, many=True)
    total = serializers.IntegerField()

    def create(self, validated_data):
        from lost_and_found.serializers.item import ItemSerializer
        items_val = []
        items_list_val = validated_data.pop("items", [])
        for each_data in items_list_val:
            each_obj = deserialize(ItemSerializer, each_data, many=False, partial=True)
            items_val.append(each_obj)

        return ItemListResponseType(items=items_val, **validated_data)
