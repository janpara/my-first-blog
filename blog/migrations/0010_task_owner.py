# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150824_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(null=True, related_name='parentasks', to='blog.Parent'),
        ),
    ]
