# Generated by Django 4.0.6 on 2023-04-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app_print', '0005_remove_uploadedfile_nconverted'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='is_converted',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
