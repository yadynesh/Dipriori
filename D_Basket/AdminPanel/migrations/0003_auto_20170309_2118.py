# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0002_auto_20170309_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_id',
            field=models.EmailField(max_length=40),
        ),
    ]