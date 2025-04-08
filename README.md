# Simple Console Chatbot

A console-based chatbot that uses OpenRouter API with Gemini model to answer user questions.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

## Usage

1. Make sure your virtual environment is activated
2. Run the chatbot:
```bash
python src/chatbot.py
```
3. Type your questions and press Enter
4. Type 'quit' or 'exit' to end the conversation

## Requirements

- Python 3.8 or higher
- OpenRouter API key
- Internet connection 