# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0024_statistic_run_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='most_frequent_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Item'),
        ),
    ]
