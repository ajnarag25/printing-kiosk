# Generated by Django 4.0.6 on 2023-04-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app_print', '0002_admin_password_admin_price_admin_timer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='converted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]