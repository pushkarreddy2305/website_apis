from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def member_info(request):
    print(request)
    from lost_and_found.serializers.id_name import IdNameSerializer
    from lost_and_found.utils.deserialize import deserialize
    request_data = deserialize(IdNameSerializer, request.data)

    from lost_and_found.models.member import Member
    obj = Member.get_member_details_by_username(request_data.username)
    from lost_and_found.serializers.user_profile import UserProfileType
    member_type_obj = UserProfileType(**obj)
    from lost_and_found.serializers.user_profile import UserProfileSerializer
    result = UserProfileSerializer(member_type_obj)
    return Response(result.data)