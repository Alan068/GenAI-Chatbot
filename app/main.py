import streamlit as st
from services.chat_service import ChatService

st.title("AI Chatbot")

chat_service = ChatService()

character = st.selectbox("Choose a character:", list(chat_service.prompts.keys()))
user_input = st.text_input("Ask something: ")

if st.button("Send"):
    if user_input:
        response = chat_service.chat_response(character, user_input)
        st.write(f"**{character}:** {response}")
