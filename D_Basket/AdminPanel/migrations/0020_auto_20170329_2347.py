# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0019_auto_20170329_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='discount',
            new_name='discount_percent',
        ),
    ]
