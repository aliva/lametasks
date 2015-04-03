from django.contrib import admin
from .models import Task
from .models import List

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "priority",
        "status",
        "list",
    )
    readonly_fields = (
        "owner",
        "completed_on",
    )

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.owner = request.user
        obj.name = obj.name.strip()
        if len(obj.name) == 0:
            return
        obj.save()

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    readonly_fields = (
        "owner",
    )

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.owner = request.user
        obj.name = obj.name.strip()
        if len(obj.name) == 0:
            return
        obj.save()