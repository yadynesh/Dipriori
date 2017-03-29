# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0014_auto_20170329_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='left_item1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_item1', to='AdminPanel.Item', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='left_item2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_item2', to='AdminPanel.Item', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='right_item1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_item1', to='AdminPanel.Item', verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='right_item2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_item2', to='AdminPanel.Item', verbose_name='Item'),
        ),
    ]
