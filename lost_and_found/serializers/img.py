from rest_framework import serializers


class ImgType(object):
    def __init__(self, image,  **kwargs):
        self.image = image


    def __unicode__(self):
        return str(self)

    def __str__(self):
        return str(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class ImgSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def create(self, validated_data):
        return ImgType(**validated_data)
