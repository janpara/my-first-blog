# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='S', max_length=1, choices=[('S', 'Sin asignar'), ('P', 'Pendiente'), ('R', 'Realizada')]),
        ),
    ]
