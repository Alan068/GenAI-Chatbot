from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
