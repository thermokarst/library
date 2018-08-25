# Generated by Django 2.1 on 2018-08-25 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0005_add_including_manager_plugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pluginauthorship',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_author_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pluginauthorship',
            name='plugin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugin_author_list', to='plugins.Plugin'),
        ),
    ]
