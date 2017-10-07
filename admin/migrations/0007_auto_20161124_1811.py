# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-24 18:11
from __future__ import unicode_literals

from django.db import migrations
import djangoplus.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0006_organization_organizationrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=djangoplus.db.models.fields.BooleanField(default=True, verbose_name='Superusu\xe1rio?'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=djangoplus.db.models.fields.CharField(max_length=128, verbose_name='Senha'),
        ),
    ]
