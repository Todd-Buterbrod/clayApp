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
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
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
    serializer = ProfileUpdateSerializer(instance=profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)