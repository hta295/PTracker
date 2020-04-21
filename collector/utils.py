from dateutil import tz

from django.http import HttpResponseRedirect
from django.urls import reverse


def convert_intervals_from_utc_to_localtime(local_tz, intervals):
    """Takes a list of UTC Intervals and converts local-timestamps in-place

    Note: This state change is local and not written to db

    :param local_tz: the local timezone
    :param intervals: the list of utc intervals
    :returns: the list of intervals with their timestamps converted
    """
    from_tz = tz.tzutc()
    for i in intervals:
        i.start_time = i.start_time.replace(tzinfo=from_tz).astimezone(local_tz)
        i.end_time = i.end_time.replace(tzinfo=from_tz).astimezone(local_tz)
    return intervals


def check_authentication(func):
    """Function decorator that checks if user is authenticated and redirects them to login page if not

    Use for functions that require authentication

    :param func: the function to decorate
    :returns: the decorated function
    """
    def decorated_func(request):
        return func(request) if request.user.is_authenticated else HttpResponseRedirect(reverse('login'))

    return decorated_func
