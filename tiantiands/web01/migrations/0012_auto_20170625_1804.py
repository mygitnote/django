# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web01', '0011_auto_20170625_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='isConment',
            field=models.BooleanField(default=False),
        ),
    ]