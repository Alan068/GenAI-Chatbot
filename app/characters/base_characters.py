from utils.utils import load_prompts


class BaseCharacter:
    def __init__(self, character_type: str, prompt_file="app/templates/prompts.yaml"):
        self.character_type = character_type
        self.prompts = load_prompts(prompt_file)


    @property    # Turns method into attribute type, no need to use (), used when need to use 'self'
    def prompt(self) -> str:
        return self.prompts.get(self.character_type, "")


    def build_prompt(self, message: str) -> str:     # build final prompt for engineeer or doctor
        return f"{self.prompts}\nUser: {message}"

