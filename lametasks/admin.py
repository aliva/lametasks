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
        "due_date",
        "list",
        "status",
    )
    readonly_fields = (
        "status",
        "owner",
        "completed_on",
        "deleted_on",
    )
    ordering = (
        "status",
        "-priority",
        "name",
    )
    actions = (
        "mark_as_done",
        "set_priority_high",
        "set_priority_normal",
        "set_priority_low",
        "set_priority_none",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj):
        if obj.status == Task.STATUS.active:
            return self.readonly_fields
        return self.list_display + self.readonly_fields

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

    def set_priority_none(self, request, queryset):
        queryset.change_priority(Task.PRIORITY.none)

    def set_priority_low(self, request, queryset):
        queryset.change_priority(Task.PRIORITY.low)

    def set_priority_normal(self, request, queryset):
        queryset.change_priority(Task.PRIORITY.normal)

    def set_priority_high(self, request, queryset):
        queryset.change_priority(Task.PRIORITY.high)

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    readonly_fields = (
        "owner",
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.owner = request.user
        obj.name = obj.name.strip()
        if len(obj.name) == 0:
            return
        obj.save()