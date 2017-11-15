from rest_framework import serializers


class LimitOffsetType(object):
    def __init__(self, offset, limit, **kwargs):
        self.offset = offset
        self.limit = limit

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LimitOffsetSerializer(serializers.Serializer):
    limit = serializers.IntegerField(default=20)
    offset = serializers.IntegerField()

    def create(self, validated_data):
        return LimitOffsetType(**validated_data)