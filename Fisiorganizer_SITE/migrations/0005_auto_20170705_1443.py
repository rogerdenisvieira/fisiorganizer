# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-05 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fisiorganizer_SITE', '0004_auto_20170704_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='surname',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
