# Generated by Django 4.1.2 on 2023-06-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_post_quill_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_quill',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
