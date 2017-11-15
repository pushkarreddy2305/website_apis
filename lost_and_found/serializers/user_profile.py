from rest_framework import serializers


class UserProfileType(object):
    def __init__(self, username, first_name, last_name, email,city, **kwargs):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.city = city

    def __unicode__(self):
        return str(self)


    def __getitem__(self, item):
        return getattr(self, item)


class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    city = serializers.CharField()

    def create(self, validated_data):
        return UserProfileType(**validated_data)
