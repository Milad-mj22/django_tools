# Generated by Django 4.1.2 on 2023-06-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_post_quill_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_quill',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
