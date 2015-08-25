# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150825_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organize',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('event', models.ForeignKey(to='blog.Event', related_name='eventorganizes')),
                ('parent', models.ForeignKey(to='blog.Parent', related_name='parentorganizes')),
            ],
        ),
    ]
