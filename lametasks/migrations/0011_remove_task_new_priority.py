# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0010_auto_20150403_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='new_priority',
        ),
    ]
