# AI Chatbot with GCP Vertex AI

This project demonstrates how to build an AI chatbot using GCP Vertex AI's `gemini-1.0-pro` model and Streamlit.

## Introduction

The AI Chatbot project leverages Google Cloud Platform's Vertex AI and the `gemini-1.0-pro` model to create an interactive, real-time chatbot. This chatbot can handle various natural language tasks, providing accurate and relevant responses to user queries. The integration with Streamlit offers a simple and intuitive interface for user interaction.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/rohanreddy1201/AI-Chatbot.git
    cd AI-Chatbot
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Google Cloud credentials**:
    - Download your GCP credentials service account key, and copy the contents into a `secrets.toml` file.
    - Place your `secrets.toml` file in the `.streamlit` directory.
    - Make sure to include the `secrets.toml` file in your .gitignore file!

5. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

## Usage

Once the Streamlit app is running, users can interact with the chatbot through a web interface. Simply enter a query into the text input box and click "Send" to receive a response. The chat history is maintained for context, and example queries are provided to help users get started.

## Capabilities

- **Natural Language Understanding**: The chatbot can understand and process user queries in natural language.
- **Real-Time Interaction**: Provides instant responses to user inputs, making the interaction seamless and engaging.
- **Contextual Awareness**: Maintains a history of the conversation to provide contextually relevant responses.
- **Secure Credentials Management**: Uses Streamlit secrets to handle Google Cloud credentials securely.

## Model Details

- **Model Used**: `gemini-1.0-pro`
- **Provider**: Google Cloud Platform's Vertex AI
- **Capabilities**: Handles various natural language processing tasks including text generation, summarization, and interactive conversation.

## Deployment

Deploy this app using Streamlit Cloud:
- Push your project to GitHub.
- Go to Streamlit Cloud, create a new app, and connect it to your GitHub repository.
- Configure secrets in Streamlit Cloud using the contents of your `secrets.toml`.

## Security

Ensure `.streamlit/secrets.toml` is never committed to the repository.
