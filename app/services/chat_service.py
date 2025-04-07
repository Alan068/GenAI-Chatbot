import yaml
from factory.concrete_creator import ModelFactory

class ChatService:
    def __init__(self, model_name="llama-3.2", prompt_file="app/templates/prompts.yaml"):   # Constructor initialises chatbot with llama and yaml file
        self.model = ModelFactory(model_name).create_model()
        self.prompts = self.load_prompts(prompt_file)

    def load_prompts(self, prompt_file):
        with open(prompt_file, "r") as file:
            return yaml.safe_load(file)   # Converted YAML to dictionary with built-in function safe_load

    def chat_response(self, character, user_input):
        if character not in self.prompts:
            return "Character not found."
        prompt = f"{self.prompts[character]}\nUser: {user_input}"
        return self.model.generate(prompt)
