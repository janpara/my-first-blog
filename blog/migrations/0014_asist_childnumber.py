# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_asist'),
    ]

    operations = [
        migrations.AddField(
            model_name='asist',
            name='childnumber',
            field=models.IntegerField(default=0),
        ),
    ]
