# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='', max_length=155),
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(default='', max_length=155),
        ),
    ]
