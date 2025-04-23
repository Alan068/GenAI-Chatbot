from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["chatbot"]
chat_collection = db["chats"]

def save_chat(session_id, character, user_input, bot_response):
    chat_collection.insert_one({
        "session_id": session_id,
        "character": character,
        "user": user_input,
        "bot": bot_response
    })

def get_recent_chats(session_id, character, limit=5):
    return list(chat_collection.find({
        "session_id": session_id,
        "character": character
    }).sort("_id", -1).limit(limit))
