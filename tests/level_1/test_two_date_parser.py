import datetime

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    assert compose_datetime_from('today', '12:45') == datetime.datetime(2024, 6, 3, 12, 45)
    assert compose_datetime_from('tomorrow', '12:45') == datetime.datetime(2024, 6, 4, 12, 45)
