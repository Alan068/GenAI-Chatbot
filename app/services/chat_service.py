from app.db.mongodb import save_chat, get_recent_chats


class ChatService:
    def __init__(self, character, model, session_id, metadata=None):
        self.character = character
        self.model = model
        self.session_id = session_id
        self.metadata = metadata


    def chat_response(self, user_input: str) -> str:
        context = self.build_context()
        print("=== CONTEXT ===")    # debug
        print(context)
        print("================")
        print("Session ID:", self.session_id)
        print("Character:", self.character.character_type)    # debug

        full_prompt = f"{self.character.prompt}\n\n{context}User: {user_input}\nBot:"
        response = self.model.generate_response(full_prompt)
        save_chat(self.session_id, self.character.character_type, user_input, response, self.metadata)
        return response


    def build_context(self):
        past_chats = get_recent_chats(self.session_id, self.character.character_type)
        print("Recent chats found:", len(past_chats))   # debug

        context = ""
        for chat in reversed(past_chats):
            context += f"User: {chat['user']}\nBot: {chat['bot']}\n"
        return context


