import streamlit as st
import json
from google.oauth2 import service_account
from vertexai import init
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Load service account credentials from Streamlit secrets
credentials_info = json.loads(st.secrets["gcp"]["service_account"])
credentials = service_account.Credentials.from_service_account_info(credentials_info)

# Initialize Vertex AI client
project_id = st.secrets["gcp"]["project_id"]
location = st.secrets["gcp"]["location"]

init(project=project_id, location=location, credentials=credentials)

model = GenerativeModel("gemini-1.0-pro")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str):
    response = chat.send_message(prompt)
    return response.text

# Streamlit app
st.title("AI Chatbot with GCP Vertex AI")

# Example queries
st.subheader("Example Queries")
st.write("- Find a weather website and tell me the weather in Portland today")
st.write("- Tell me a joke.")
st.write("- What is AI?")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
st.subheader("Chat History")
for i, (user_input, response) in enumerate(st.session_state.chat_history):
    st.write(f"**You:** {user_input}")
    st.write(f"**Chatbot:** {response}")

# Text input at the bottom
st.write("##")
user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        response = get_chat_response(chat, user_input)
        st.session_state.chat_history.append((user_input, response))
        st.rerun()  # Use st.rerun instead of st.experimental_rerun
    else:
        st.write("Please enter your query.")
