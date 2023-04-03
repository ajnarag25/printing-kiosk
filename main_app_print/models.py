from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    uploaded_file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class admin_price(models.Model):
    black = models.IntegerField()
    colored = models.IntegerField()


class admin_password(models.Model):
    type = models.CharField(max_length=255)
    password = models.IntegerField()


class admin_timer(models.Model):
    time = models.IntegerField()
