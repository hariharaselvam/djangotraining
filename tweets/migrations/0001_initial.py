# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 05:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Account')),
                ('hashtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.Hashtag')),
            ],
        ),
    ]
