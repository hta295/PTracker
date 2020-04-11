from dateutil import tz

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .utils import convert_intervals_from_utc_to_localtime


def index(request):
    if request.user.is_authenticated:
        # TODO: Get tz from the user request.
        # tzlocal() uses the TIME_ZONE from settings.py and not the end-user
        intervals = convert_intervals_from_utc_to_localtime(tz.tzlocal(),
                        request.user.interval_set.all().order_by('-start_time'))
        return render(request, 'collector/index.html', {'interval_list': intervals})
    else:
        return HttpResponseRedirect('../login')
