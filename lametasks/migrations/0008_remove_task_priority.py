# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0007_auto_20150403_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
    ]
