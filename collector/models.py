from django.contrib.auth.models import User

from django.db import models


class Interval(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField('starting time')
    end_time = models.DateTimeField('ending time')

    def compute_delta(self):
        """Computes the time delta between the starting and ending time

        :returns: a datetime timedelta object representing the time interval
        """
        return self.end_time - self.start_time

    def __str__(self):
        time_format = '%b %d, %Y, %I:%M:%S %p'
        return f'{self.start_time.strftime(time_format)} - {self.end_time.strftime(time_format)}'
