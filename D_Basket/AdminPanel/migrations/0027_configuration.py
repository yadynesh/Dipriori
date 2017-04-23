# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0026_statistic_total_batches'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_email_id', models.EmailField(max_length=100, verbose_name='Email address')),
                ('server_ip_addrress', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(re.compile('^(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(\\.(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}\\Z', 32), 'Enter a valid IPv4 address.', 'invalid')], verbose_name='Item Name')),
            ],
        ),
    ]