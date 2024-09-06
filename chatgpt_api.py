# chatgpt_api.py

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Instantiate OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def get_response(conversation_history, agent_role):
    """Get response from ChatGPT based on the conversation history and agent role."""
    # Insert the system role message at the start of the conversation history
    messages = [{"role": "system", "content": agent_role}] + conversation_history

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return response.choices[0].message.content
