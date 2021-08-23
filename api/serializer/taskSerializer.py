from rest_framework import serializers
from api.models.taskModels import Task
from .profileSerializer import ProfileUsernameAndIdSerializer



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

class TaskListByProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('header', 'time', 'done', 'rejected', 'id', 'profile')

class TaskGetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('header', 'time', 'daily', 'day_of_week', 'description', 'done', 'rejected', 'created', 'id')

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('header', 'time', 'daily', 'day_of_week', 'description')

class TaskWithUsernameSerializer(serializers.ModelSerializer):
    profile = ProfileUsernameAndIdSerializer()
    class Meta:
        model = Task
        fields = ('header', 'time', 'daily', 'day_of_week', 'description', 'done', 'rejected', 'id', 'profile')