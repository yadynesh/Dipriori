# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0028_configuration_admin_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='admin_password',
        ),
        migrations.AddField(
            model_name='configuration',
            name='admin_email_password',
            field=models.CharField(default='yadynesh123', max_length=100, verbose_name='Email address password'),
            preserve_default=False,
        ),
    ]
