# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-28 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20171228_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]