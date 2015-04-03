# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lametasks', '0004_auto_20150403_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=model_utils.fields.StatusField(default='none', no_check_for_status=True, max_length=100, choices=[(0, 'dummy')]),
        ),
    ]
