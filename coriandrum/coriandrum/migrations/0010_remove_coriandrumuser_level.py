# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-21 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coriandrum', '0009_auto_20171021_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coriandrumuser',
            name='level',
        ),
    ]
