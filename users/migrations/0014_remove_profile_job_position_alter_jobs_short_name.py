# Generated by Django 4.1.2 on 2023-06-18 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_jobs_persian_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job_position',
        ),
        migrations.AlterField(
            model_name='jobs',
            name='short_name',
            field=models.CharField(max_length=3),
        ),
    ]
