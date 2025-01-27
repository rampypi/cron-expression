from abc import ABC, abstractmethod
from typing import List

class IFieldParser(ABC):
    @abstractmethod
    def parse(self, expression: str) -> List[int]:
        pass

class ITimeField(ABC):
    @abstractmethod
    def get_range(self) -> tuple[int, int]:
        pass
    
    @abstractmethod
    def validate(self, value: int) -> bool:
        pass
