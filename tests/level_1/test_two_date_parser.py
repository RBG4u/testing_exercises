from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    # Test 1
    date_str = 'something'
    time_str = '12:30'
    expected_datetime = datetime.datetime(today.year, today.month, today.day, 12, 30)
    assert compose_datetime_from(date_str, time_str) == expected_datetime

    # Test 2: Tomorrow date
    date_str = 'tomorrow'
    time_str = '09:45'
    expected_datetime = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 9, 45)
    assert compose_datetime_from(date_str, time_str) == expected_datetime

    # Test 3: Time with spaces
    date_str = 'something'
    time_str = '   18:15    '
    expected_datetime = datetime.datetime(today.year, today.month, today.day, 18, 15)
    assert compose_datetime_from(date_str, time_str) == expected_datetime
