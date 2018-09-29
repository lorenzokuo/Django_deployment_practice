# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-28 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20180928_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cate',
            name='job',
        ),
        migrations.AddField(
            model_name='job',
            name='cate',
            field=models.CharField(default=django.utils.timezone.now, max_length=45),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cate',
        ),
    ]