import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from

@pytest.mark.parametrize(
        "name_day, time, result", 
        [
            ('today', '12:45', datetime.datetime(2024, 7, 13, 12, 45)),
            ('tomorrow', '12:45', datetime.datetime(2024, 7, 14, 12, 45)),
        ]
)
def test_compose_datetime_from(name_day, time, result):
    assert compose_datetime_from(name_day, time,) == result
