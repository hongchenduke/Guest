# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-11-03 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='addless',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='limt',
            new_name='limit',
        ),
        migrations.RenameField(
            model_name='guest',
            old_name='Event',
            new_name='event',
        ),
        migrations.AddField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
