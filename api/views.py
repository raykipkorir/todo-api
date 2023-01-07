from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from django.shortcuts import render

def api_routes(request):
    return render(request, "api/index.html")

class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

