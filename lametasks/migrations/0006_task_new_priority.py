# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0005_auto_20150403_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='new_priority',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, 'none'), (1, 'low'), (2, 'normal'), (3, 'high')]),
        ),
    ]
