# Generated by Django 4.0.6 on 2023-04-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app_print', '0006_uploadedfile_is_converted'),
    ]

    operations = [
        migrations.CreateModel(
            name='print_option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printer_name', models.CharField(max_length=255)),
                ('copies', models.IntegerField()),
                ('size', models.CharField(choices=[('letter', 'letter'), ('a4', 'a4'), ('exective', 'executive'), ('legal', 'legal')], max_length=255)),
                ('color_mode', models.CharField(choices=[('colored', 'colored'), ('grayscale', 'grayscale')], max_length=255)),
                ('rangee', models.CharField(max_length=255)),
            ],
        ),
    ]
