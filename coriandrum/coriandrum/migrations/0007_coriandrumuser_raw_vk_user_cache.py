# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coriandrum', '0006_auto_20171021_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='coriandrumuser',
            name='raw_vk_user_cache',
            field=models.TextField(blank=True, default=''),
        ),
    ]
