# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0025_statistic_most_frequent_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='total_batches',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]