# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('booking_date', models.DateField()),
                ('booking_slot', models.TimeField()),
                ('dt', models.DateTimeField()),
            ],
        ),
    ]
