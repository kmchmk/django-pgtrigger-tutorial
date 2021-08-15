# Generated by Django 3.0.8 on 2020-07-23 01:41

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        (
            "tutorial",
            "0001_initial",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="FSM",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            (
                                "unpublished",
                                "Unpublished",
                            ),
                            (
                                "published",
                                "Published",
                            ),
                            (
                                "inactive",
                                "Inactive",
                            ),
                        ],
                        default="unpublished",
                        max_length=16,
                    ),
                ),
            ],
        ),
    ]
