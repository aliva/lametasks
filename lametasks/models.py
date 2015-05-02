from django.db import models
from model_utils import Choices

class Task(models.Model):
    name = models.CharField(max_length=140)

    STATUS = Choices(
        (1, "active", "active"),
        (2, "done", "done")
    )
    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS.active)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)