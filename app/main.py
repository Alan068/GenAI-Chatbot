import streamlit as st
from factory import ChatbotFactory


st.title("AI Chatbot")


character = st.selectbox("Choose a character:", list(ChatbotFactory.get_characters()))
user_input = st.text_input("Ask something: ")


if st.button("Send"):
    if user_input:
        chatbot = ChatbotFactory.create(character_type=character, model_type="llama3.2")
        response = chatbot.chat_response(user_input)
        st.write(f"**{character}:** {response}")
