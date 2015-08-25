# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_organize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('event', models.ForeignKey(to='blog.Event', related_name='eventasists')),
                ('pupil', models.ForeignKey(to='blog.Pupil', related_name='pupilasists')),
            ],
        ),
    ]
