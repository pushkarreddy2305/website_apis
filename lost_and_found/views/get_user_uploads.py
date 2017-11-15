from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def get_user_uploads(request,username):
    from lost_and_found.serializers.limit_offset import LimitOffsetSerializer
    from lost_and_found.utils.deserialize import deserialize
    request_data = deserialize(LimitOffsetSerializer, request.data)

    from lost_and_found.models.item import Item

    items_query_set = Item.objects.filter(uploaded_by__username=username,is_found=False)
    total = len(items_query_set)
    obj = {
        "items": items_query_set,
        "total": total
    }
    from lost_and_found.serializers.item_list import ItemListResponseType
    item_type_obj = ItemListResponseType(**obj)
    from lost_and_found.serializers.item_list import ItemListResponseSerializer
    result = ItemListResponseSerializer(item_type_obj)
    return Response(result.data)