# Generated by Django 4.1.2 on 2023-06-13 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_post_quill_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_quill',
            name='author',
        ),
    ]
