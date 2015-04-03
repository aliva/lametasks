from django.conf import settings
from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

class BaseClass(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(BaseClass):
    name = models.CharField(max_length=140)
    completed_on = models.DateTimeField(blank=True, null=True)
    list = models.ForeignKey("List", blank=True, null=True)
    STATUS = Choices(
        "active",
        "done",
    )
    status = StatusField(choices_name="STATUS", default=STATUS.active)
    PRIORITY = Choices(
        "none",
        "low",
        "normal",
        "high",
    )
    priority = StatusField(choices_name="PRIORITY", default=PRIORITY.none)

class List(BaseClass):
    name = models.CharField(max_length=140)

    class Meta:
        unique_together = ("name", "owner")
