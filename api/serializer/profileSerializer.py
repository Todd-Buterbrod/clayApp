from rest_framework import serializers
import re
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
    # def validate(self, data):
    #     good_username = [a-z0-9\_]
    #     if data[Profile.username] != good_username:
    #         raise serializers.ValidationError("Можно применить только A-Z, a-z, 0-9, _ символы")
    #     return data
    class Meta:
        model = Profile
        fields = ('username', 'alternative_name', 'bio', 'date_of_birth', 'id')


