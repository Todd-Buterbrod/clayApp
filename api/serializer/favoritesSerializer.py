from rest_framework import serializers
from api.models.favoritesModels import Favorite
from .taskSerializer import TaskSerializer
from .profileSerializer import ProfileUsernameAndIdSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteShowAllSerializer(serializers.ModelSerializer):
    profile = ProfileUsernameAndIdSerializer()
    favorite_task = TaskSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'

