# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('admin', '0009_auto_20170420_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
            ],
            options={
                'verbose_name': 'Permiss\xe3o',
                'proxy': True,
                'verbose_name_plural': 'Permiss\xf5es',
                'indexes': [],
            },
            bases=('auth.permission',),
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
    ]
