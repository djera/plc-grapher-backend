# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170103_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('production', 'production'), ('marketing', 'marketing')], default='admin', max_length=155),
        ),
    ]
