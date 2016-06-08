# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-07 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('authors', models.ManyToManyField(to='ask.Author', verbose_name='\u0410\u0432\u0442\u043e\u0440\u044b')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': '\u041b\u0430\u0439\u043a', 'verbose_name_plural': '\u041b\u0430\u0439\u043a\u0438'},
        ),
    ]