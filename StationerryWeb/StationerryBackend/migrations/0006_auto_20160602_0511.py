# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-02 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StationerryBackend', '0005_users_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='User_Name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Name', to='StationerryBackend.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='App_Name',
            field=models.TextField(),
        ),
    ]
