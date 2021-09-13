from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/images', null=False, max_length=1028*1028, blank=False)