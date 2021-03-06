# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-10 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20171010_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodelconfig',
            name='config',
        ),
        migrations.RemoveField(
            model_name='variableconfig',
            name='name',
        ),
        migrations.AddField(
            model_name='datamodelconfig',
            name='name',
            field=models.CharField(default='default', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='variableconfig',
            name='config',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.DataModelConfig'),
            preserve_default=False,
        ),
    ]
