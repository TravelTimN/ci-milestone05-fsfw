# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-14 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_auto_20190713_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='gross_total',
        ),
        migrations.AddField(
            model_name='ticket',
            name='total_donations',
            field=models.IntegerField(default=0),
        ),
    ]