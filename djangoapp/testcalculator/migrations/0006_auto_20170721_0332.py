# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcalculator', '0005_auto_20170721_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='institution',
            field=models.TextField(max_length=75),
        ),
    ]
