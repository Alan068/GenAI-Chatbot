from factory.creator import BaseModelFactory
from factory.product import BaseModel
from factory.models import LlamaModel

class ModelFactory(BaseModelFactory):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def create_model(self) -> BaseModel:
        if self.model_name == "llama-3.2":
            return LlamaModel()
        else:
            raise ValueError(f"Model '{self.model_name}' is not supported.")
