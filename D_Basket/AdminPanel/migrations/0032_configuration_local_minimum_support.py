# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0031_auto_20170423_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='local_minimum_support',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]