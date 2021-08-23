from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from api.paginations import PaginationById

from api.models.followingModels import Following
from api.models.profileModels import Profile
from api.serializer.followingSerializer import FollowingSerializer, FollowingShowAllSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Following Create': 'create/',
        'Following List': 'list/',
        'Following Get By Id': 'get-by-id/<str:pk>/',
        'Following Get By Followed Id': 'get-by-followed-id/<str:pk>/',
        'Following Get By Followers Id': 'get-by-followers-id/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def followingCreate(request):
    serializer = FollowingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def followingList(request):
    paginator = PaginationById()
    followings = Following.objects.all()
    context = paginator.paginate_queryset(followings, request)
    serializer = FollowingShowAllSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def followingGetById(request, pk):
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
