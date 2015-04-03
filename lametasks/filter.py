from django.contrib import admin
from .models import Task

class TaskStatusListFilter(admin.SimpleListFilter):
    title = "Status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return Task.STATUS + ("all",)

    def queryset(self, request, queryset):
        if self.value() == "all":
            return queryset
        if self.value() is None:
            return queryset.filter(status=Task.STATUS.active)
        return queryset.filter(status=self.value())
    def choices(self, cl):
        yield {
            'selected': self.value() is None,
            'query_string': cl.get_query_string({}, [self.parameter_name]),
            'display': 'active',
        }
        for lookup, title in self.lookup_choices:
            if lookup == "active":
                continue
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }