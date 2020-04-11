from dateutil import tz

from .models import Interval


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
