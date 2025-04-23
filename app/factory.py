from characters.base_characters import BaseCharacter
from models.llama_model import LlamaModel
from services.chat_service import ChatService
from utils.utils import load_prompts


class ChatbotFactory:
    @staticmethod
    def create(character_type: str, model_type: str = "llama-3.2") -> ChatService:
        def create_character():
            return BaseCharacter(character_type)

        model_map = {
            "llama3.2": LlamaModel,
        }

        model_class = model_map.get(model_type.lower())
        if not model_class:
            raise ValueError(f"Unsupported model: {model_type}")

        model = model_class(model_type)

        character = create_character()
        return ChatService(character, model)


    @staticmethod
    def get_characters():
        prompts = load_prompts()
        return list(prompts.keys())