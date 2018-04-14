# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-13 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0002_vendor_area_code'),
        ('news_subscription', '0008_auto_20180412_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribepaper',
            name='vendor',
            field=models.ForeignKey(default='000', on_delete=django.db.models.deletion.CASCADE, related_name='myvendor', to='Vendor.Vendor', verbose_name='Vendor'),
        ),
    ]