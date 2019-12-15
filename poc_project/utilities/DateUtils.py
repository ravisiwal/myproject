from typing import List, Tuple, Any
# import arrow
# from arrow import Arrow
import re
from datetime import datetime, timedelta
from dateutil import parser, tz


def calc_date(date: datetime, add=True, **kwargs):
    """
    add/subtract date interval from date
    :param date: The date (year, month, or day, for example) that the function operates on
    :param add:
        True: add date operation
        False: subtract date operation
    :param kwargs: timedelta arguments, days, seconds, microseconds, milliseconds, minutes, hours, weeks
    :return:
    """
    return date + timedelta(**kwargs) if add else date - timedelta(**kwargs)


def get_contiguous_date_ranges(dates: List[Tuple[Any, Any]]):
    """
    :param dates: list of tuples of (start_date, end_date) [which will be parsed by arrow.get]
    :return: list of contiguous date ranges in the form [(start_date1, end_date1), (start_date2, end_date2), ...]
    """
    res = []
    dates = [(arrow.get(sd), arrow.get(ed)) for sd, ed in dates]
    dates.sort()

    cur_start = cur_end = None
    for sd, ed in dates:
        if cur_start is None:
            cur_start, cur_end = sd, ed
        else:
            if sd > cur_end:
                res.append((cur_start, cur_end))
                cur_start, cur_end = sd, ed
            else:
                cur_end = max(cur_end, ed)
    else:
        if cur_start:
            res.append((cur_start, cur_end))

    return res


def get_date_range_from_lookback_days(start_date: Arrow, lookback_days: int) -> List[Arrow]:
    """
    gets a list of dates from given date and days to lookback
    :return: a list of dates for the given range
    """
    run_date = arrow.get(start_date, 'YYYY/MM/DD')
    start_date = run_date.replace(days=-lookback_days)

    return Arrow.range('day', start_date, run_date)


def convert_ordinaldate_date(date: str):
    """
    :param dates: date string in ordinal date format
    :return: date string in strptime format
    """
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', date)


def convert_string_to_date(date: str):
    """
    Convert date string to datetime object
    :param date: Feb 8th, 2018 3:12 am or 8 February 2018, 3:12 am or Feb 8th, 2018
    :return: datetime.datetime(2018, 2, 8, 3, 12)
    """
    return parser.parse(date.strip())


def compare_date(x: str, y: str, offset: int = 60, x_tz: str = None, y_tz: str = None) -> bool:
    """
    Function to compare time difference between x in utc timezone,  y in utc timezone over offset.
    :param x: time one
    :param y: time two
    :param offset: x and y difference
    :param x_tz: timezone for time one
    :param y_tz: timezone for time two
    :return: True x smaller or equal to y, False, x larger than y
    """
    date_cmp = list()
    try:
        for i in [(x, x_tz), (y, y_tz)]:
            if not i[1] or i[1] != 'UTC':
                date_cmp.append(convert_string_to_date(date=i[0]).astimezone(tz.gettz('UTC')))
            else:
                date_cmp.append(convert_string_to_date(date=i[0]))

        return int(abs(date_cmp[0] - date_cmp[1]).total_seconds()) <= offset
    except ValueError:
        raise ValueError("Incorrect Time format on Last Login")


def get_system_timezone():
    return tz.tzlocal()
