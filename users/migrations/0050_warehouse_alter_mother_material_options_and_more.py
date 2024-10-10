# Generated by Django 5.0.7 on 2024-09-29 14:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_profile_address_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='mother_material',
            options={'ordering': ['describe']},
        ),
        migrations.AlterModelOptions(
            name='raw_material',
            options={'ordering': ['describe']},
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory_raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='users.raw_material')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='users.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_type', models.CharField(choices=[('ADD', 'افزودن'), ('REMOVE', 'برداشتن')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='users.inventory')),
            ],
        ),
    ]