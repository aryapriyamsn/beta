# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-13 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userinfo_area_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email_id',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]