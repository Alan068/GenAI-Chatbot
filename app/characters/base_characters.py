from utils.utils import load_prompts


class BaseCharacter:
    def __init__(self, character_type: str, prompt_file="app/templates/prompts.yaml"):
        self.character_type = character_type
        self.prompts = load_prompts(prompt_file)


    def build_prompt(self, message: str) -> str:     # Fetches and build prompt for engineeer or doctor
        character_prompt = self.prompts.get(self.character_type, "")
        return f"{character_prompt}\nUser: {message}"

