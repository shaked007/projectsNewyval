from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import  IsAuthenticated

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response({'success':'User logged out successfully'})

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getGroups(request):
    data = {'groups':[]}
    data['groups'] = [str(group) for group in request.user.groups.all()]
    # for group in request.user.groups.all():
    #     print(str(group))
        #groups.append(group)
    return JsonResponse(data)