# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-27 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0022_auto_20190721_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
