import ollama
from factory.product import BaseModel

class LlamaModel(BaseModel):
    def generate(self, prompt: str) -> str:
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

# Later on more models to be added

