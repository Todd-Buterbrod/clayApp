from rest_framework import serializers
from api.models.followingModels import Following
from .profileSerializer import ProfileUsernameAndIdSerializer


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'

class FollowingShowAllSerializer(serializers.ModelSerializer):
    author = ProfileUsernameAndIdSerializer()
    follower = ProfileUsernameAndIdSerializer()

    class Meta:
        model = Following
        fields = '__all__'