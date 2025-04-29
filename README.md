# GenAI-Chatbot
A multi-character AI chatbot built with Streamlit and powered by Llama 3.2 via Ollama (For now). Prompts are managed using YAML files for each character (e.g., Engineer, Doctor) and a factory pattern is used to support scalable model integration.

# Features
- Context-based chat history using MongoDB
- Multiple character support (Engineer, Doctor)
- YAML-based prompt system
- Factory pattern for easy model/character expansion
- Streamlit-based frontend


# Installation

1. Clone the Repo   
git clone https://github.com/alan068/genai-chatbot.git  
cd genai-chatbot

2. Create and Activate Virtual Environment  
python -m venv venv  (In VS Code Terminal)
. venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
or
manually install following libraries:
pip install pyyaml   (In VS Code Terminal)
pip install ollama
pip install streamlit
pip install pymongo

4. Ollama Setup
Install and run Ollama locally from: https://ollama.com/

Then in cmd
To check version: ollama --version
To check models: ollama list
To run model 3.2: ollama run llama3.2
To stop: ctrl+c

5. MongoDB Setup
Make sure MongoDB is installed and running locally
To connect mongodb database:

open cmd, write this comand > mongod
keep this cmd open and running in bg
A 'chatbot' database and 'chats' collection will be auto-created on first run.

6. Run the App
streamlit run main.py
will open at Local URL: http://localhost:8501


# Future Add ons
More AI models support like GPT model
Instead of passing last 5 convo, maybe switch to summarization for context based chat
Use Browser cookies instead of session ID


# Author -> ALAN SHIBU
Made during internship at Grey Chain

