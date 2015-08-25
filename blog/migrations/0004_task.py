# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(related_name='tasks', to='blog.Event')),
            ],
        ),
    ]
