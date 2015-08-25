# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_asist_childnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asist',
            name='event',
        ),
        migrations.RemoveField(
            model_name='asist',
            name='pupil',
        ),
        migrations.RemoveField(
            model_name='organize',
            name='event',
        ),
        migrations.RemoveField(
            model_name='organize',
            name='parent',
        ),
        migrations.AddField(
            model_name='parent',
            name='eventsassisted',
            field=models.ManyToManyField(related_name='parentassists', to='blog.Event'),
        ),
        migrations.AddField(
            model_name='parent',
            name='eventsorganized',
            field=models.ManyToManyField(related_name='parentorganizes', to='blog.Event'),
        ),
        migrations.AddField(
            model_name='pupil',
            name='eventsassisted',
            field=models.ManyToManyField(to='blog.Event'),
        ),
        migrations.DeleteModel(
            name='Asist',
        ),
        migrations.DeleteModel(
            name='Organize',
        ),
    ]
