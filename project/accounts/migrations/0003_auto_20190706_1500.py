# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-06 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190702_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_imgs/default.png', null=True, upload_to='profile_imgs'),
        ),
    ]
