from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def member_login(request):
    from lost_and_found.serializers.log_in import LoginSerializer
    from lost_and_found.utils.deserialize import deserialize
    request_data = deserialize(LoginSerializer, request.data)

    from lost_and_found.models.member import Member
    member = Member.login(request_data)
    member_obj = {
        "id": member.id,
        "username": member.user
    }
    from lost_and_found.serializers.id_name import IdNameType
    member_id = IdNameType(**member_obj)

    from lost_and_found.serializers.id_name import IdNameSerializer
    member_id_serializer = IdNameSerializer(member_id)

    return Response(member_id_serializer.data)

