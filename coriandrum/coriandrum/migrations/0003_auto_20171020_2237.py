# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coriandrum', '0002_auto_20171020_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coriandrumuser',
            name='vk_user_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
