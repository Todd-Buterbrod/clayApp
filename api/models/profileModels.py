from django.db import models


class Profile(models.Model):
    username = models.CharField(max_length=24, unique=True)
    alternative_name = models.CharField(max_length=24)
    bio = models.CharField(max_length=60)
    date_of_birth = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    followers = models.IntegerField(default=0)
    followed = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.username