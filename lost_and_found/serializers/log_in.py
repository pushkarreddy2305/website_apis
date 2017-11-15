from rest_framework import serializers


class LoginType(object):
    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password

    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        return LoginType(**validated_data)