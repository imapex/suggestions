# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-21 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0005_submission_spark_room_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='spark_room_url',
            field=models.URLField(blank=True),
        ),
    ]
