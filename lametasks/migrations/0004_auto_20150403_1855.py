# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0003_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.SmallIntegerField(choices=[(0, 'none'), (1, 'low'), (2, 'normal'), (3, 'high')], default=0),
        ),
    ]
