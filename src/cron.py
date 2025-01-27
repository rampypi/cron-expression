from dataclasses import dataclass
from typing import List
from src.fields import MinuteField, HourField, DayOfMonthField, MonthField, DayOfWeekField
from src.cron_parser import ExpressionParser

@dataclass
class CronExpression:
    minute: str
    hour: str
    day_of_month: str
    month: str
    day_of_week: str
    command: str

    def parse(self) -> dict:
        parsers = {
            'minute': ExpressionParser(MinuteField()),
            'hour': ExpressionParser(HourField()),
            'day of month': ExpressionParser(DayOfMonthField()),
            'month': ExpressionParser(MonthField()),
            'day of week': ExpressionParser(DayOfWeekField())
        }

        expressions = {
            'minute': self.minute,
            'hour': self.hour,
            'day of month': self.day_of_month,
            'month': self.month,
            'day of week': self.day_of_week
        }

        result = {}
        for field_name, expression in expressions.items():
            result[field_name] = parsers[field_name].parse(expression)
        
        return result

    def format_output(self) -> str:
        parsed = self.parse()
        output = []
        
        for field_name, values in parsed.items():
            output.append(f"{field_name:<14} {' '.join(map(str, values))}")
        
        output.append(f"{'command':<14} {self.command}")
        return '\n'.join(output)
