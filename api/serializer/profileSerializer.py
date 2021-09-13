from rest_framework import serializers
from api.models.profileModels import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileUsernameAndIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'id')

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'alternative_name', 'bio', 'date_of_birth', 'id')


