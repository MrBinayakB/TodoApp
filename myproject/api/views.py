from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from mainapp.models import TaskModel
from mainapp.models import UserModel
from .serializers import TaskSerializer, UserSerializer

#GET and POST method for Task
@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = TaskModel.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def tasks_detail(request, pk):

    try:
        tasks = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(tasks)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(tasks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Get and POST method for USer
@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        user = UserModel.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def users_detail(request, pk):

    try: 
        user = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer  = UserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)