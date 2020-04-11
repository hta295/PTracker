import datetime
import itertools
import pytz

from unittest.mock import MagicMock
from django.test import TestCase
from django.utils import timezone

from .models import Interval, User
from .utils import convert_intervals_from_utc_to_localtime


class IntervalModelTests(TestCase):

    def test_compute_delta(self):
        start = timezone.now()
        end = timezone.now()
        mock_user = MagicMock(spec=User)
        mock_user._state = MagicMock()
        i = Interval(start_time=start, end_time=end, user=mock_user)
        expected = end - start
        actual = i.compute_delta()
        self.assertEqual(expected, actual)


def get_interval():
    mock_user = MagicMock(spec=User)
    mock_user._state = MagicMock()
    while True:
        start = timezone.now()
        end = timezone.now()
        yield Interval(start_time=start, end_time=end, user=mock_user)


class UtilTests(TestCase):

    def test_convert_intervals_from_utc_to_localtime(self):
        mock_user = MagicMock(spec=User)
        mock_user._state = MagicMock()
        utc_intervals = list(itertools.islice(get_interval(), 5))
        expected_starts = [i.start_time - datetime.timedelta(hours=4) for i in utc_intervals]
        expected_ends = [i.end_time - datetime.timedelta(hours=4) for i in utc_intervals]
        local_tz = pytz.timezone('US/Eastern')
        converted_intervals = convert_intervals_from_utc_to_localtime(local_tz, utc_intervals.copy())
        for (expected_start, expected_end, converted) in zip(expected_starts, expected_ends, converted_intervals):
            self.assertEqual(expected_start.timetuple()[:8], converted.start_time.timetuple()[:8])
            self.assertEqual(expected_end.timetuple()[:8], converted.end_time.timetuple()[:8])
