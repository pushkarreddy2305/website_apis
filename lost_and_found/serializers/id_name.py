from rest_framework import serializers


class IdNameType(object):
    def __init__(self, username, id=None, **kwargs):
        self.id = id
        self.username = username


    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class IdNameSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()

    def create(self, validated_data):
        return IdNameType(**validated_data)
