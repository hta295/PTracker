from datetime import datetime
from dateutil import tz

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Interval
from .utils import convert_intervals_from_utc_to_localtime
from .utils import check_authentication as check_auth


@check_auth
def index(request):
    # TODO: Get tz from the user request.
    # tzlocal() uses the TIME_ZONE from settings.py and not the end-user
    intervals = convert_intervals_from_utc_to_localtime(tz.tzlocal(),
                                                        request.user.interval_set.all().order_by('-start_time'))
    return render(request, 'collector/index.html', {'interval_list': intervals})


def _validate_add(start, end):
    """Validates new interval is valid and returns an error message if it is bad

    :param start: the start timestamp for the interval
    :param end: the end timestamp for the interval

    :returns: the error_message as a string or None if interval is valid
    """
    # Add Interval to monitor only if start <= end < now. Otherwise, show user an error
    now = datetime.now()
    error_message = None
    if end >= now:
        error_message = 'New interval should be in the past'
    elif end < start:
        error_message = 'Starting time should be before ending time'
    return error_message


@check_auth
def add(request):
    """View for user to add a new Interval.

    POST tries to add an interval, otherwise the view just displays an entry form that, in-turn, POST's to this view
    Interval should be 'valid' s.t. start_time <= end_time < now

    :param request: the incoming HTTP request

    :returns: appropriate HTTP response
    """
    if request.method == 'POST':
        input_time_format = '%Y-%m-%dT%H:%M'
        start = datetime.strptime(request.POST['start_time'], input_time_format)
        end = datetime.strptime(request.POST['end_time'], input_time_format)
        error_message = _validate_add(start, end)
        if not error_message:
            # Add interval and redirect to index
            i = Interval(user=request.user, start_time=start, end_time=end)
            i.save()
            return HttpResponseRedirect(reverse('collector:index'))
        else:
            # Show page again with an error
            return render(request, 'collector/add.html', {'error_message': error_message})
    else:
        return render(request, 'collector/add.html')
