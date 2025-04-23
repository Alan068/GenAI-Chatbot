class ChatService:
    def __init__(self, character, model):
        self.character = character
        self.model = model

    def chat_response(self, user_input: str) -> str:
        prompt = self.character.build_prompt(user_input)
        response = self.model.generate_response(prompt)
        return response
