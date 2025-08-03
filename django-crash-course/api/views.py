# api/views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    Una única ViewSet para ver, editar y eliminar tareas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer