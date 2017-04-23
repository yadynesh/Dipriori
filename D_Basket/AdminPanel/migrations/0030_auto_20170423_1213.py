# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:43
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0029_auto_20170423_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='server_ip_addrress',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile('^(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(\\.(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}\\Z', 32), 'Enter a valid IPv4 address.', 'invalid')], verbose_name='Server IP Address'),
        ),
    ]
