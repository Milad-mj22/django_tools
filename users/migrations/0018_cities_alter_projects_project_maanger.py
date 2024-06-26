# Generated by Django 4.1.2 on 2023-06-19 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('persian_name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'ordering': ['-short_name'],
            },
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_maanger',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_city', to='users.cities'),
        ),
    ]
