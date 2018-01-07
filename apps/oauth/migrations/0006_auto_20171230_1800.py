# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-30 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0005_auto_20171230_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouser',
            name='link',
            field=models.URLField(blank=True, help_text='网址必须填写以http开头的完整形式', verbose_name='个人网址'),
        ),
    ]