# Generated by Django 5.0.7 on 2024-07-27 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_mode_raw_materials_alter_raw_material_mother'),
    ]

    operations = [
        migrations.AddField(
            model_name='raw_material',
            name='mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mode_raw_materials_id', to='users.mode_raw_materials'),
        ),
        migrations.AlterField(
            model_name='raw_material',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother_material', to='users.mother_material'),
        ),
    ]
