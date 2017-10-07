# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 17:50
from __future__ import unicode_literals

from django.db import migrations
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_auto_20160914_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='default_color',
        ),
        migrations.AddField(
            model_name='settings',
            name='sidebar_fixed',
            field=djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Fixo'),
        ),
        migrations.AddField(
            model_name='settings',
            name='sidebar_hidden',
            field=djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Escondido'),
        ),
        migrations.AddField(
            model_name='settings',
            name='sidebar_mini',
            field=djangoplus.db.models.fields.BooleanField(default=False, verbose_name='Compacto'),
        ),
        migrations.AddField(
            model_name='settings',
            name='theme',
            field=djangoplus.db.models.fields.CharField(choices=[[b'skin-6', b'skin-6'], [b'skin-5', b'skin-5']], default=b'skin-6', max_length=255, verbose_name='Tema'),
        ),
    ]
