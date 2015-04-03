from django.contrib import admin
from .filter import TaskStatusListFilter
from .models import Task
from .models import List

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = (
        TaskStatusListFilter,
        "priority",
        "list",
    )
    list_display = (
        "name",
        "priority",
        "status",
        "list"
    )
    readonly_fields = (
        "status",
        "owner",
        "completed_on",
        "deleted_on",
    )
    ordering = (
        "status",
        "priority",
        "name",
    )
    actions = (
        "mark_as_done",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.owner = request.user
        obj.name = obj.name.strip()
        if len(obj.name) == 0:
            return
        obj.save()

    def delete_model(self, request, obj):
        obj.change_status(Task.STATUS.deleted)

    def mark_as_done(self, request, queryset):
        queryset.change_status(Task.STATUS.done)

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