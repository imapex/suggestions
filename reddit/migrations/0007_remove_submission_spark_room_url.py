# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-21 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0006_auto_20160821_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='spark_room_url',
        ),
    ]
