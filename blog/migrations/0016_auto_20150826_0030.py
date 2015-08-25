# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150825_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='eventsassisted',
            field=models.ManyToManyField(to='blog.Event', related_name='parentassists', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='eventsorganized',
            field=models.ManyToManyField(to='blog.Event', related_name='parentorganizes', null=True, blank=True),
        ),
    ]
