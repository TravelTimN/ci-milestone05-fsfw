# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-11 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20190711_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='', help_text='Comments can have a maximum of 2,000 characters.', max_length=2000, null=True),
        ),
    ]
