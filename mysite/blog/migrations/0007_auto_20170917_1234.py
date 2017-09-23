# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-17 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_crawler_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawler',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
