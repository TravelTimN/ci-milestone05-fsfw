# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-07 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20190707_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]