# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition_info',
            name='num',
            field=models.CharField(default=12, max_length=10),
            preserve_default=False,
        ),
    ]
