# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170823_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_pokes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
