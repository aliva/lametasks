# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('completed_on', models.DateTimeField(null=True, blank=True)),
                ('status', model_utils.fields.StatusField(max_length=100, choices=[('active', 'active'), ('done', 'done')], default='active', no_check_for_status=True)),
                ('priority', model_utils.fields.StatusField(max_length=100, choices=[('none', 'none'), ('low', 'low'), ('normal', 'normal'), ('high', 'high')], default='none', no_check_for_status=True)),
                ('list', models.ForeignKey(to='lametasks.List', null=True, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([('name', 'owner')]),
        ),
    ]
