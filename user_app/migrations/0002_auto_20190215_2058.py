# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import user_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=user_app.models.pics_directory_path),
        ),
    ]
