# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 23:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coriandrum', '0014_auto_20171021_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='in_consideration_by_moderator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='is_considered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('new', 'Новый пост'), ('in_consideration', 'Заблокирован редактором на осознание'), ('looks_interesting', 'Понравился редактору'), ('trash', 'В топке'), ('published', 'Опубликован'), ('invalid', 'Не валиден')], default='new', max_length=25),
        ),
    ]
