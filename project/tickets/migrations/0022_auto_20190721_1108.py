# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-21 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_auto_20190718_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketstatus',
            options={'verbose_name': 'Ticket Status', 'verbose_name_plural': 'Ticket Status'},
        ),
        migrations.AlterModelOptions(
            name='tickettype',
            options={'verbose_name': 'Ticket Type', 'verbose_name_plural': 'Ticket Types'},
        ),
    ]
