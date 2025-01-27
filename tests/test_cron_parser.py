import pytest
from src.cron import CronExpression

def test_basic_every_15_minutes():
    expression = CronExpression("*/15", "0", "1,15", "*", "1-5", "/usr/bin/find")
    result = expression.parse()
    assert result['minute'] == [0, 15, 30, 45]

def test_every_nth_hour():
    expression = CronExpression("0", "*/4", "*", "*", "*", "/usr/bin/test")
    result = expression.parse()
    assert result['hour'] == [0, 4, 8, 12, 16, 20]

def test_range_with_steps():
    expression = CronExpression("0", "9-17/2", "*", "*", "*", "/usr/bin/test")
    result = expression.parse()
    assert result['hour'] == [9, 11, 13, 15, 17]

def test_multiple_ranges():
    expression = CronExpression("0", "0", "1-5,10-15", "*", "*", "/usr/bin/test")
    result = expression.parse()
    assert result['day of month'] == [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]

def test_all_fields_asterisk():
    expression = CronExpression("*", "*", "*", "*", "*", "/usr/bin/test")
    result = expression.parse()
    assert len(result['minute']) == 60
    assert len(result['hour']) == 24
    assert len(result['day of month']) == 31
    assert len(result['month']) == 12
    assert len(result['day of week']) == 7

def test_invalid_minute_range():
    with pytest.raises(ValueError):
        expression = CronExpression("60", "*", "*", "*", "*", "/usr/bin/test")
        expression.parse()

def test_invalid_hour_range():
    with pytest.raises(ValueError):
        expression = CronExpression("0", "24", "*", "*", "*", "/usr/bin/test")
        expression.parse()

def test_invalid_day_range():
    with pytest.raises(ValueError):
        expression = CronExpression("0", "0", "32", "*", "*", "/usr/bin/test")
        expression.parse()

def test_invalid_month_range():
    with pytest.raises(ValueError):
        expression = CronExpression("0", "0", "*", "13", "*", "/usr/bin/test")
        expression.parse()

def test_invalid_step_value():
    with pytest.raises(ValueError):
        expression = CronExpression("*/0", "*", "*", "*", "*", "/usr/bin/test")
        expression.parse()

def test_complex_combinations():
    expression = CronExpression("*/15", "0-12/3", "1,15", "*/4", "1-5", "/usr/bin/test")
    result = expression.parse()
    assert result['minute'] == [0, 15, 30, 45]
    assert result['hour'] == [0, 3, 6, 9, 12]
    assert result['day of month'] == [1, 15]
    assert result['month'] == [1, 5, 9]
    assert result['day of week'] == [1, 2, 3, 4, 5]

def test_single_values():
    expression = CronExpression("5", "10", "15", "3", "2", "/usr/bin/test")
    result = expression.parse()
    assert result['minute'] == [5]
    assert result['hour'] == [10]
    assert result['day of month'] == [15]
    assert result['month'] == [3]
    assert result['day of week'] == [2]

def test_overlapping_ranges():
    expression = CronExpression("0", "0", "1-15,10-20", "*", "*", "/usr/bin/test")
    result = expression.parse()
    expected_days = list(range(1, 21))
    assert result['day of month'] == expected_days

def test_step_with_range():
    expression = CronExpression("0", "0", "1-30/5", "*", "*", "/usr/bin/test")
    result = expression.parse()
    assert result['day of month'] == [1, 6, 11, 16, 21, 26]

def test_command_with_arguments():
    command = "/usr/bin/find /path -name '*.txt' -type f"
    expression = CronExpression("0", "0", "*", "*", "*", command)
    result = expression.format_output()
    assert command in result
