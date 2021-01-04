# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0027_auto_20180412_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='numberofdays',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='option4',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
