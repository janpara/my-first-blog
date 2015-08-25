# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150824_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='pupil',
            field=models.ForeignKey(to='blog.Pupil', related_name='parents'),
        ),
    ]
