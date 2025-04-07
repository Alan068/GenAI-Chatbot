from abc import ABC, abstractmethod
from factory.product import BaseModel

class BaseModelFactory(ABC):
    @abstractmethod
    def create_model(self) -> BaseModel:
        pass
