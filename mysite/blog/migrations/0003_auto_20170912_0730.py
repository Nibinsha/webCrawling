# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-12 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_crawler_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawler',
            name='Pic',
            field=models.ImageField(upload_to='/home/nibinsha/Documents/CRAWLER/mysite/static/images/'),
        ),
    ]
