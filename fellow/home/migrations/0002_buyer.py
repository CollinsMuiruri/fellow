# Generated by Django 4.1.2 on 2022-10-07 12:47

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buyer",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("home.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
