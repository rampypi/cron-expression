from typing import List
from src.interfaces import IFieldParser, ITimeField

class ExpressionParser(IFieldParser):
    def __init__(self, field: ITimeField):
        self.field = field

    def parse(self, expression: str) -> List[int]:
        if expression == '*':
            return self._handle_asterisk()
        
        values = set()
        for part in expression.split(','):
            if '-' in part:
                values.update(self._handle_range(part))
            elif '/' in part:
                values.update(self._handle_step(part))
            else:
                values.add(self._handle_single_value(part))
                
        result = sorted(list(values))
        self._validate_values(result)
        return result

    def _handle_asterisk(self) -> List[int]:
        min_val, max_val = self.field.get_range()
        return list(range(min_val, max_val + 1))

    def _handle_range(self, expression: str) -> List[int]:
        # Handle cases like "9-17/2"
        if '/' in expression:
            range_part, step = expression.split('/')
            start, end = map(int, range_part.split('-'))
            step = int(step)
            return list(range(start, end + 1, step))
        
        # Handle regular ranges like "1-5"
        start, end = map(int, expression.split('-'))
        return list(range(start, end + 1))

    def _handle_step(self, expression: str) -> List[int]:
        start_expr, step = expression.split('/')
        step = int(step)
        
        if start_expr == '*':
            min_val, max_val = self.field.get_range()
            return list(range(min_val, max_val + 1, step))
        
        start = int(start_expr)
        min_val, max_val = self.field.get_range()
        return list(range(start, max_val + 1, step))

    def _handle_single_value(self, value: str) -> int:
        return int(value)

    def _validate_values(self, values: List[int]) -> None:
        for value in values:
            if not self.field.validate(value):
                raise ValueError(f"Value {value} is out of range for this field")
