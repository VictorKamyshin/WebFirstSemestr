# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0018_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='static/media/images/'),
        ),
    ]
