from django.db import models
from datetime import timedelta
from django.conf import settings

# Create your models here.


class Task(models.Model):

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Task\'s'

    STATUSES = (
        (1, 'Started'),
        (2, 'Completed'),
        (3, 'Paused'),
        (4, 'Unknown')
    )

    id = models.PositiveIntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    time_elapsed = models.DurationField(default=timedelta)
    status = models.SmallIntegerField(verbose_name='Task\'s status',
                                      choices=STATUSES)
    is_complete = models.BooleanField(verbose_name='Task ended.', default=False)

    def __str__(self):
        return self.title
