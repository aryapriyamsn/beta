# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-14 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('Vendor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(related_name='vendor_is', to='users.Users', verbose_name='customer')),
                ('vendor', models.ManyToManyField(related_name='of_customer', to='Vendor.Vendor', verbose_name='vendor')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
