# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-28 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20171212_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_id',
            field=models.CharField(default='user100', max_length=20),
            preserve_default=False,
        ),
    ]
