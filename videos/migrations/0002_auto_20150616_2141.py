# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-year']},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='descriptiom',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='date',
        ),
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='year',
            field=models.PositiveSmallIntegerField(default=2015),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='event',
            field=models.ForeignKey(blank=True, null=True, to='videos.Event'),
        ),
    ]
