# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 22:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clipboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clip',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clips', to=settings.AUTH_USER_MODEL),
        ),
    ]