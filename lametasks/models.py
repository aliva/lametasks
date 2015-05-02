from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils import Choices
from model_utils.fields import StatusField

class BaseClass(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TaskQuerySet(models.QuerySet):
    def change_status(self, status):
        self.update(status=status)
        if status == Task.STATUS.done:
            self.update(deleted_on=None)
            self.filter(completed_on__isnull=True).update(completed_on=timezone.now())
        if status == Task.STATUS.archived:
            pass

    def change_priority(self, priority):
        self.filter(status=Task.STATUS.active).update(priority=priority)

class Task(BaseClass):
    objects = TaskQuerySet.as_manager()

    name = models.CharField(max_length=140)
    due_date = models.DateField(blank=True, null=True)
    completed_on = models.DateTimeField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey("List", blank=True, null=True)
    STATUS = Choices(
        "active",
        "done",
        "archived",
        "deleted",
    )
    status = StatusField(choices_name="STATUS", default=STATUS.active)
    PRIORITY = Choices(
        (0, "none", "none"),
        (1, "low", "low"),
        (2, "normal", "normal"),
        (3, "high", "high"),
    )
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=PRIORITY.none)
    postponed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def change_status(self, status):
        self.status = status
        if status == Task.STATUS.deleted:
            self.postponed=0
            self.completed_on=None
            self.due_date=None
            self.name="DELETED"
            self.list=None
            self.priority=Task.PRIORITY.none
            if self.deleted_on is None:
                self.deleted_on=timezone.now()
        self.save()

    def postpone(self):
        if self.status != Task.STATUS.active:
            return
        now = timezone.now().date()
        if self.due_date is None or self.due_date < now:
            self.due_date = now
        else:
            self.due_date += timezone.timedelta(1)
        self.postponed += 1
        self.save()

class List(BaseClass):
    name = models.CharField(max_length=140)

    class Meta:
        unique_together = ("name", "owner")

    def __str__(self):
        return self.name