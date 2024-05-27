# Generated by Django 4.1.2 on 2023-06-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="tools",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("content", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Publish")], default=0
                    ),
                ),
            ],
            options={
                "ordering": ["-title"],
            },
        ),
    ]
