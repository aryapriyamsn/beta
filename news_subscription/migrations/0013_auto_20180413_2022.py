# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-13 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0012_auto_20180413_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribepaper',
            name='vendor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Vendor.Vendor', to_field='VIN'),
        ),
    ]