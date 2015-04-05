# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0011_remove_task_new_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='postponed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
