from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check(request, username,item_name,item_category):
    from lost_and_found.serializers.img import ImgSerializer
    from lost_and_found.utils.deserialize import deserialize
    request_data = deserialize(ImgSerializer, request.data)

    print(request_data.image)
    from lost_and_found.models.item import Item
    item_obj = Item.create_item(item_name,item_category,username,request_data.image)
    print(type(item_obj.item_image))
    item= Item.get_item_details(item_obj.id)
    from lost_and_found.serializers.img import ImgType
    member_id = ImgType(**item)

    from lost_and_found.serializers.img import ImgSerializer
    member_id_serializer = ImgSerializer(member_id)

    return Response(member_id_serializer.data)


