"""
Simple console chatbot using OpenRouter API with Mistral model.
Following PEP 8 style guide and project standards.
"""
import os
from typing import Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# this is function defined by learner
def initialize_chat() -> Optional[ChatOpenAI]:
    """
    Initialize the chat model with OpenRouter API.
    
    Returns:
        Optional[ChatOpenAI]: Configured chat model instance or None if setup fails
    """
    print("Hello, beautiful learner")
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found in .env file")
        return None
    
    return ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        model="mistralai/mistral-7b-instruct",
        streaming=True,
        max_tokens=1000  # Limiting max tokens to stay within free tier limits
    )

# this is function defined by learner
def chat_loop(chat_model: ChatOpenAI) -> None:
    """
    Main chat loop for interaction with the user.
    
    Args:
        chat_model (ChatOpenAI): The initialized chat model instance
    """
    print("Hello, beautiful learner")
    print("\nWelcome to the Simple Console Chatbot!")
    print("Type 'quit' or 'exit' to end the conversation")
    print("-" * 50)

    system_message = SystemMessage(content="You are a helpful AI assistant.")

    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue

        try:
            messages = [
                system_message,
                HumanMessage(content=user_input)
            ]
            response = chat_model.invoke(messages)
            print(f"\nAssistant: {response.content}")
        except Exception as e:
            print(f"\nError: {str(e)}")

# this is function defined by learner
def main() -> None:
    """
    Main function to run the chatbot application.
    """
    print("Hello, beautiful learner")
    chat_model = initialize_chat()
    if chat_model:
        chat_loop(chat_model)

if __name__ == "__main__":
    main() 