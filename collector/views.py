from dateutil import tz

from django.views import generic

from .models import User, Interval
from .utils import convert_intervals_from_utc_to_localtime


class IndexView(generic.ListView):
    template_name = 'collector/index.html'

    def get_queryset(self):
        utc_intervals = User.objects.get(pk=1).interval_set.all().order_by('-start_time')
        # TODO: Get tz from the user request.
        # tzlocal() uses the TIME_ZONE from settings.py and not the end-user
        return convert_intervals_from_utc_to_localtime(tz.tzlocal(), utc_intervals)
