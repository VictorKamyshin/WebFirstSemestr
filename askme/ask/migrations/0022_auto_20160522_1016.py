# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0021_auto_20160522_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
