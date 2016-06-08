# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 11:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask', '0006_auto_20160508_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question_Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u041b\u0430\u0439\u043a',
                'verbose_name_plural': '\u041b\u0430\u0439\u043a\u0438',
            },
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]