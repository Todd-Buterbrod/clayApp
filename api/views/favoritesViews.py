from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from api.models.favoritesModels import Favorite
from api.paginations import PaginationById
from api.serializer.favoritesSerializer import FavoriteSerializer
from api.serializer.favoritesSerializer import FavoriteShowAllSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Favorites Create': 'create/',
        'Favorites Delete': 'delete/<str:pk>/',
        'Favorites List': 'list/',
        'Favorites Get By Id': 'get/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['POST'])
def favoritesCreate(request):
    serializer = FavoriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def favoritesDelete(request, pk):
    favorite = Favorite.objects.get(id=pk)
    favorite.delete()
    return Response("The Task Deleted From Favorites")

@api_view(['GET'])
def favoritesList(request):
    paginator = PaginationById()
    favorites = Favorite.objects.all()
    context = paginator.paginate_queryset(favorites, request)
    serializer = FavoriteShowAllSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def favoritesGetById(request, pk):
    favorite = Favorite.objects.all().filter(profile=pk)
    serializer = FavoriteShowAllSerializer(favorite, many=True)
    return Response(serializer.data)