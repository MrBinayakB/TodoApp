from rest_framework.response import Response
from rest_framework.decorators import api_view
from mainapp.models import TaskModel
from mainapp.models import UserModel
from .serializers import TaskSerializer, UserSerializer

#GET and POST method for Task
@api_view(['GET'])
def getTask(request):
    tasks = TaskModel.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Get and POST method for USer
@api_view(['GET'])
def getUser(request):
    tasks = UserModel.objects.all()
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)