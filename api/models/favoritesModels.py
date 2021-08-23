from django.db import models
from .taskModels import Task
from .taskModels import Profile

class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='profile')
    favorite_task = models.ForeignKey(Task, on_delete=models.PROTECT, related_name='favorite_task')

    def __str__(self):
        return self.profile


