from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

def index(request):
    return render(request, "lametasks/index.html")

class TaskViewSet(viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def list(self, request):
        qs = self.get_queryset()
        qs = qs.filter(status=Task.STATUS.active)
        return Response(TaskSerializer(qs, many=True).data)