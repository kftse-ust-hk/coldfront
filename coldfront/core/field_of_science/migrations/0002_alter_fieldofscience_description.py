# SPDX-FileCopyrightText: (C) ColdFront Authors
#
# SPDX-License-Identifier: AGPL-3.0-or-later

# Generated by Django 3.2.17 on 2023-04-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("field_of_science", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fieldofscience",
            name="description",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
