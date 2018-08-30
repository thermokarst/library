# Generated by Django 2.1 on 2018-08-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0018_more_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plugin',
            name='name',
            field=models.CharField(help_text="The plugin's name, as registered in QIIME 2.", max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='plugin',
            name='title',
            field=models.CharField(help_text="The plugin's project title.", max_length=500, unique=True),
        ),
    ]
