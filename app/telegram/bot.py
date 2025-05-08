import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, ConversationHandler, filters, CallbackQueryHandler)
from app.factory import ChatbotFactory


load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


CHOOSING, CHATTING = range(2)  # Telegram bot conversation states
user_sessions = {}


logging.basicConfig(level=logging.INFO)

CHARACTER_EMOJIS = {
    "Doctor": "🩺",
    "Engineer": "🛠️",
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    characters = ChatbotFactory.get_characters()
    buttons = [
        [InlineKeyboardButton(f"{CHARACTER_EMOJIS.get(char, '')} {char}", callback_data=char)]
        for char in characters
    ]

    await update.message.reply_text(
        "Welcome to CASE 🤖! Choose a character to begin:",
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    return CHOOSING



async def choose_character(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    username = query.from_user.username or query.from_user.full_name or "unknown"
    character = query.data

    session_id = f"telegram_{user_id}"
    metadata = {
        "user_id": user_id,
        "username": username
    }

    # Saving users chosen character
    user_sessions[user_id] = {
        "character": character,
        "chatbot": ChatbotFactory.create(character, "llama3.2", session_id=session_id, metadata=metadata)
    }

    await query.edit_message_text(f"Great! You're now chatting with {CHARACTER_EMOJIS.get(character, '')} {character}. Ask away!")
    return CHATTING



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text

    if user_id not in user_sessions:
        await update.message.reply_text("Please choose a character first using /start.")
        return CHOOSING

    chatbot = user_sessions[user_id]["chatbot"]
    response = chatbot.chat_response(message)
    await update.message.reply_text(response)
    return CHATTING



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Chat ended. Use /start to begin again.")
    return ConversationHandler.END



def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING: [CallbackQueryHandler(choose_character)],
            CHATTING: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    app.run_polling()   # Continuously sending HTTP req to telegram servers to fetch updates


if __name__ == "__main__":   # Only runs when bot.py is executed directly. "python -m app.telegram.bot"
    main()