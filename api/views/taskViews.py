from rest_framework import generics, permissions
from datetime import datetime, date, timedelta
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from api.paginations import PaginationByCreateTime

from api.models.taskModels import Task
from api.serializer.taskSerializer import TaskSerializer
from api.serializer.taskSerializer import TaskListByProfileSerializer
from api.serializer.taskSerializer import TaskGetDetailSerializer
from api.serializer.taskSerializer import TaskWithUsernameSerializer
from api.serializer.taskSerializer import TaskUpdateSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Task Create': '/create/',
        'Task Get': '/get/<str:pk>/',
        'Task Get Detail': '/get-detail/<str:pk>/',
        'Task Update': '/update/<str:pk>/',
        'Task List': '/list/',
        'Task List By Profile': '/list/<str:pk>/',
        'Task Delete': '/delete/<str:pk>/',
        'Task Get With Username': '/get-with-username/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def taskGet(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def taskGetDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskGetDetailSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def taskList(request):
    paginator = PaginationByCreateTime()
    tasks = Task.objects.all().filter(deleted=False)
    context = paginator.paginate_queryset(tasks, request)
    serializer = TaskWithUsernameSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def taskListByProfile(request, pk):
    paginator = PaginationByCreateTime()
    tasks = Task.objects.all().filter(profile=pk, deleted=False)
    context = paginator.paginate_queryset(tasks, request)
    serializer = TaskListByProfileSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Deleted Successfully")

@api_view(['GET'])
def taskGetWithUsername(request, pk):
    paginator = PaginationByCreateTime()
    task = Task.objects.all().filter(profile=pk, deleted=False)
    context = paginator.paginate_queryset(task, request)
    serializer = TaskWithUsernameSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    try:
        task = Task.objects.get(id=pk)
        timeblock = task.created + timedelta(minutes=5)
        my_datetime = datetime.now()
        if my_datetime.date() == timeblock.date() and my_datetime.time() <= timeblock.time():
            serializer = TaskUpdateSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data="Истекло время редактирования")
    except:
        return Response(status=status.HTTP_404_NOT_FOUND, data="Запись не найдена")

