import re

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from api.models.profileModels import Profile
from api.paginations import PaginationById, PaginationByCreateTime
from api.serializer.profileSerializer import ProfileSerializer
from api.serializer.profileSerializer import ProfileUpdateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Profile Create': '/create/',
        'Profile List': '/list/',
        'Profile Get': '/get/<str:pk>/',
        'Profile Update': '/update/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def profileCreate(request):
    username = request.data.get("username")
    regex = r'^[a-z0-9_]{1,24}$'
    pattern = re.compile(regex)
    if not re.match(pattern, username):
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data="Имя пользователя должно состоять из 1-24 символов и может содержать только строчные буквы латинского алфавита от a до z, цифры от 0 до 9 и символ нижнего подчеркивания _")
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="Такое имя уже существует")
    return Response(serializer.data)

@api_view(['GET'])
def profileList(request):
    paginator = PaginationByCreateTime()
    profiles = Profile.objects.all()
    context = paginator.paginate_queryset(profiles, request)
    serializer = ProfileSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def profileGet(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profileUpdate(request, pk):
    profile = Profile.objects.get(id=pk)
    username = request.data.get("username")
    regex = r'^[a-z0-9_]{1,24}$'
    pattern = re.compile(regex)
    if not re.match(pattern, username):
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data="Имя пользователя должно состоять из 1-24 символов и может содержать только строчные буквы латинского алфавита от a до z, цифры от 0 до 9 и символ нижнего подчеркивания _")
    serializer = ProfileUpdateSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data="Такое имя уже существует")
    return Response(serializer.data)