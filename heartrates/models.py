from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class HeartrateReading(models.Model):
    position = models.CharField(max_length=20)
    heartrate = models.IntegerField()
    date_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Heartrate'