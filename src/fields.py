from src.interfaces import ITimeField

class MinuteField(ITimeField):
    def get_range(self) -> tuple[int, int]:
        return (0, 59)
    
    def validate(self, value: int) -> bool:
        min_val, max_val = self.get_range()
        return min_val <= value <= max_val

class HourField(ITimeField):
    def get_range(self) -> tuple[int, int]:
        return (0, 23)
    
    def validate(self, value: int) -> bool:
        min_val, max_val = self.get_range()
        return min_val <= value <= max_val

class DayOfMonthField(ITimeField):
    def get_range(self) -> tuple[int, int]:
        return (1, 31)
    
    def validate(self, value: int) -> bool:
        min_val, max_val = self.get_range()
        return min_val <= value <= max_val

class MonthField(ITimeField):
    def get_range(self) -> tuple[int, int]:
        return (1, 12)
    
    def validate(self, value: int) -> bool:
        min_val, max_val = self.get_range()
        return min_val <= value <= max_val

class DayOfWeekField(ITimeField):
    def get_range(self) -> tuple[int, int]:
        return (0, 6)
    
    def validate(self, value: int) -> bool:
        min_val, max_val = self.get_range()
        return min_val <= value <= max_val
