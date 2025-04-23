import streamlit as st
from factory import ChatbotFactory
import uuid


st.title("AI Chatbot")


if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

character = st.selectbox("Choose a character:", list(ChatbotFactory.get_characters()))
user_input = st.text_input("Ask something: ")


if st.button("Send"):
    if user_input:
        chatbot = ChatbotFactory.create(character_type=character, model_type="llama3.2", session_id=st.session_state.session_id)
        response = chatbot.chat_response(user_input)
        st.write(f"**{character}:** {response}")
