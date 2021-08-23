from django.db import models
from .profileModels import Profile


class Following(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='author')
    follower = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='follower')

    def __str__(self):
        return self.follower

