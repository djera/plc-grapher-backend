# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20170104_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('production', 'production'), ('marketing', 'marketing')], default='admin', max_length=155),
        ),
    ]
