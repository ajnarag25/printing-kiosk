from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    uploaded_file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_converted = models.IntegerField()


class admin_price(models.Model):
    black = models.IntegerField()
    colored = models.IntegerField()


class admin_timer(models.Model):
    time = models.IntegerField()


class print_option(models.Model):
    size = [
        ('letter', 'letter'),
        ('a4', 'a4'),
        ('exective', 'executive'),
        ('legal', 'legal'),
    ]
    color_mode = [
        ('colored', 'colored'),
        ('grayscale', 'grayscale'),
    ]
    printer_name = models.CharField(max_length=255)
    copies = models.IntegerField()
    size = models.CharField(max_length=255, choices=size)
    color_mode = models.CharField(max_length=255, choices=color_mode)
    rangee = models.CharField(max_length=255)
