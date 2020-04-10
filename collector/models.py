from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username


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
        return f'{self.start_time} - {self.end_time}'
