from django.db import models
from .profileModels import Profile


class Task(models.Model):
    header = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=2000, null=True)
    daily = models.BooleanField(default=False, blank=True, null=False)
    day_of_week = models.CharField(max_length=60, default="[]")
    time = models.TimeField(null=False)
    edit_time = models.BooleanField(default=False, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    done = models.IntegerField()
    rejected = models.IntegerField()
    deleted = models.BooleanField(default=False, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.header