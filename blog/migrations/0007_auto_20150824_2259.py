# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_task_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, default='M')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='pupil',
            field=models.ForeignKey(related_name='parents', to='blog.Pupil'),
        ),
]
