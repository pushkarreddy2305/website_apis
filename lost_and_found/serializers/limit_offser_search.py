from rest_framework import serializers


class LimitOffsetType(object):
    def __init__(self, offset, limit, search, filter_by="all", **kwargs):
        self.offset = offset
        self.limit = limit
        self.filter_by = filter_by
        self.search = search

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LimitOffsetSearchSerializer(serializers.Serializer):
    limit = serializers.IntegerField(default=20)
    offset = serializers.IntegerField()
    filter_by = serializers.CharField(allow_null=True, required=False)
    search = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        return LimitOffsetType(**validated_data)
