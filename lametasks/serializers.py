from rest_framework import serializers
from .models import List
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    priority = serializers.SerializerMethodField()

    class Meta:
        model = Task
        exclude = (
            "owner",
        )

    def get_priority(self, obj):
        return obj.get_priority_display()