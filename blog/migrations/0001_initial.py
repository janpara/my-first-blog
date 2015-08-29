# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('when', models.DateTimeField(null=True)),
                ('where', models.CharField(null=True, max_length=2000)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(related_name='eventcurso', null=True, to='blog.Curso', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('eventsassisted', models.ManyToManyField(null=True, to='blog.Event', blank=True, related_name='parentassists')),
                ('eventsorganized', models.ManyToManyField(null=True, to='blog.Event', blank=True, related_name='parentorganizes')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1)),
                ('curso', models.ForeignKey(related_name='pupilstudies', null=True, to='blog.Curso', blank=True)),
                ('eventsassisted', models.ManyToManyField(null=True, to='blog.Event', blank=True, related_name='pupilassists')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('S', 'Sin asignar'), ('P', 'Pendiente'), ('R', 'Realizada')], default='S', max_length=1)),
                ('budget', models.FloatField(default=0.0)),
                ('event', models.ForeignKey(to='blog.Event', related_name='tasks')),
                ('owner', models.ForeignKey(related_name='parentasks', null=True, to='blog.Parent', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='pupil',
            field=models.ForeignKey(to='blog.Pupil', related_name='parents'),
        ),
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='comments'),
        ),
    ]
