# Generated by Django 5.0.7 on 2024-09-30 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0053_alter_inventory_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorylog',
            name='user',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_inventory', to='users.profile'),
        ),
    ]
