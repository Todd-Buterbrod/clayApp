from rest_framework import status
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from api.models.imageModels import Image
from api.serializer.imageSerializer import ImageSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Image Upload': '/upload/',
    }
    return Response(api_urls)


class ImageList(APIView):
    parser_classes = (MultiPartParser, FileUploadParser,)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)