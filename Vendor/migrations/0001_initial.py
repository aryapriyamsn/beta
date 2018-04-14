# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vendor_pic', models.ImageField(upload_to='vendors_pic')),
                ('VIN', models.IntegerField()),
                ('address', models.TextField(default='address')),
                ('contact_no', models.IntegerField(default='0000000000')),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendors',
            },
        ),
    ]