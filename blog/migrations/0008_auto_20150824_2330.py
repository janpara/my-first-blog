# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150824_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='pupil',
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.DeleteModel(
            name='Pupil',
        ),
    ]
