# Generated by Django 4.1.2 on 2023-06-18 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_full_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_position',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
