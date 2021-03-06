# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-21 14:46
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coriandrum', '0008_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coriandrumuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[(b'new', b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xbf\xd0\xbe\xd1\x81\xd1\x82'), (b'in_consideration', b'\xd0\x97\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xbe\xd0\xba\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xbc \xd0\xbd\xd0\xb0 \xd0\xbe\xd1\x81\xd0\xbe\xd0\xb7\xd0\xbd\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'), (b'looks_interesting', b'\xd0\x9f\xd0\xbe\xd0\xbd\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd1\x81\xd1\x8f \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xbe\xd1\x80\xd1\x83'), (b'trash', b'\xd0\x92 \xd1\x82\xd0\xbe\xd0\xbf\xd0\xba\xd0\xb5'), (b'published', b'\xd0\x9e\xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd')], default=b'new', max_length=25),
        ),
    ]
