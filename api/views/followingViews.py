from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from api.paginations import PaginationById

from api.models.followingModels import Following
from api.models.profileModels import Profile
from api.serializer.followingSerializer import FollowingSerializer, FollowingShowAllSerializer
from api.serializer.profileSerializer import ProfileSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Following Create': 'create/',
        'Following Delete': 'delete/<str:pk>/',
        'Following List': 'list/',
        'Following Get': 'get/<str:pk>/',
        'Following Get By Followed Id': 'get-by-followed-id/<str:pk>/',
        'Following Get By Followers Id': 'get-by-followers-id/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def followingCreate(request):
    profile = Profile.objects.get(id=request.data.get("author"))
    profile2 = Profile.objects.get(id=request.data.get("follower"))
    profile.followed += int(1)
    profile2.followers += int(1)
    serializer = FollowingSerializer(data=request.data)
    if profile.id != profile2.id and serializer.is_valid():
        serializer.save()
        profile.save()
        profile2.save()
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data="Нельзя подписаться на самого себя или такая связь уже существует")
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def followingDelete(request, pk):
    following = Following.objects.get(id=pk)
    following.delete()
    return Response("This Following Deleted")

@api_view(['GET'])
def followingList(request):
    paginator = PaginationById()
    followings = Following.objects.all()
    context = paginator.paginate_queryset(followings, request)
    serializer = FollowingShowAllSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def followingGet(request, pk):
    following = Following.objects.all().filter(id=pk)
    serializer = FollowingShowAllSerializer(following, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def followingGetByFollowedId(request, pk):
    paginator = PaginationById()
    following = Following.objects.all().filter(author_id=pk)
    context = paginator.paginate_queryset(following, request)
    serializer = FollowingShowAllSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def followingGetByFollowersId(request, pk):
    paginator = PaginationById()
    following = Following.objects.all().filter(follower_id=pk)
    context = paginator.paginate_queryset(following, request)
    serializer = FollowingShowAllSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

