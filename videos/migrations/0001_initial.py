# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('descriptiom', models.TextField(blank=True)),
                ('website', models.URLField()),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('url', models.URLField()),
                ('event', models.ForeignKey(to='videos.Event', null=True)),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
