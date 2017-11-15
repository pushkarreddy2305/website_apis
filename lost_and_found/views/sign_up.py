from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def member_signup(request):
    from lost_and_found.serializers.signup import SignupSerializer
    from lost_and_found.utils.deserialize import deserialize
    member_obj = deserialize(SignupSerializer, request.data)

    from lost_and_found.models.member import Member
    member = Member.sign_up(member_obj)
    member_obj = {
        "id": member.id,
        "username": member.user,
        "user_type": "member"
    }
    from lost_and_found.serializers.id_name import IdNameType
    obj = IdNameType(**member_obj)

    from lost_and_found.serializers.id_name import IdNameSerializer
    obj_serializer = IdNameSerializer(obj)

    return Response(obj_serializer.data)
