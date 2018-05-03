from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def update_user_info(request,username):
    from lost_and_found.serializers.user_profile import UserProfileSerializer
    from lost_and_found.utils.deserialize import deserialize
    request_data = deserialize(UserProfileSerializer, request.data)

    from lost_and_found.models.member import Member
    obj = Member.update_profile(request_data=request_data)
    from lost_and_found.serializers.id_name import IdNameType
    member_type_obj = IdNameType(**obj)
    from lost_and_found.serializers.id_name import IdNameSerializer
    result = IdNameSerializer(member_type_obj)
    return Response(result.data)