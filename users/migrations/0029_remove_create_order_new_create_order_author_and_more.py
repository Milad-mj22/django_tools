# Generated by Django 4.2.13 on 2024-05-22 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0028_create_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='create_order',
            name='new',
        ),
        migrations.AddField(
            model_name='create_order',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_create_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='create_order',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='create_order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]