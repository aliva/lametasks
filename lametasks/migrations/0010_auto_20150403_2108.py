# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def migrate_priority(apps, schema_editor):
    Task = apps.get_model("lametasks", "Task")
    for task in Task.objects.all():
        task.priority = task.new_priority
        task.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0009_task_priority'),
    ]

    operations = [
        migrations.RunPython(migrate_priority),
    ]
