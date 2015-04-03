# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def migrate_priority(apps, schema_editor):
    Task = apps.get_model("lametasks", "Task")
    pri = {
        "none"   : 0,
        "low"    : 1,
        "normal" : 2,
        "high"   : 3,
    }
    for task in Task.objects.all():
        task.new_priority = pri[task.priority]
        task.save()

class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0006_task_new_priority'),
    ]

    operations = [
        migrations.RunPython(migrate_priority),
    ]
