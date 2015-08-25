# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, related_name='parentasks', to='blog.Parent'),
        ),
    ]
