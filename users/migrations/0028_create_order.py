# Generated by Django 4.2.13 on 2024-05-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_rename_name_material_raw_material_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.CharField(max_length=200)),
            ],
        ),
    ]
