# Simple Console Chatbot - Cursor Development Project

A sophisticated console-based chatbot developed using Cursor IDE with comprehensive development rules and standards. This project demonstrates modern AI-assisted development practices using OpenRouter API with Mistral AI model integration through LangChain.

## Project Overview

This chatbot application showcases:
- **Cursor IDE Integration**: Full utilization of Cursor's AI-powered development capabilities
- **Structured Development**: Comprehensive rule-based development approach
- **AI Integration**: OpenRouter API with Mistral-7B-Instruct model
- **Modern Python Practices**: Type hints, docstrings, and PEP 8 compliance

## Project Structure & File Descriptions

### Core Application Files

- **`src/chatbot.py`** - Main application logic containing the console chatbot implementation
  - Uses OpenRouter API with Mistral-7B-Instruct model
  - Implements proper error handling and user interaction loop
  - Features streaming responses with token limits for free tier compatibility
  - Includes initialization, chat loop, and main execution functions

### Configuration Files

- **`requirements.txt`** - Python dependencies specification
  - `langchain` - LLM integration framework
  - `python-dotenv` - Environment variable management
  - `requests` - HTTP library for API calls

- **`project-rules.txt`** - Project specification and requirements document
  - Defines chatbot functionality requirements
  - Specifies OpenRouter API integration details
  - Outlines development and testing guidelines

### Cursor IDE Development Files

- **`initialize_cursor_rules.ps1`** - PowerShell script for Cursor IDE setup
  - Automatically creates `.cursor/rules/` directory structure
  - Generates comprehensive development rules in `.mdc` format
  - Sets up `.cursorrules` file with mandatory rule application instructions
  - Ensures consistent development practices across the project

## .cursor Folder - AI Development Configuration

The `.cursor` folder contains critical configuration for Cursor IDE's AI-assisted development:

### `.cursorrules` - Master Rule Configuration
- **Purpose**: Mandatory rule application instructions for Cursor IDE
- **Key Features**:
  - Enforces rule fetching before any code changes
  - Ensures consistent AI assistance behavior
  - Manages rule type configurations and mappings
  - Provides strict guidelines for rule application

### `.cursor/rules/` Directory - Development Standards

#### `rule-standards.mdc`
- **Function**: Ensures new rules follow proper structure
- **Applies to**: All `.mdc` files
- **Requirements**: Description fields, globs patterns, coding-standards compliance

#### `rule-visibility.mdc`
- **Function**: Transparency in AI rule application
- **Requirements**: Display all applied rules at every AI action
- **Format**: Bulleted list format for rule names and descriptions

#### `rules-location.mdc`
- **Function**: Enforces proper rule file organization
- **Requirement**: All rules must be located in `.cursor/rules` directory
- **Application**: Every edit or rule creation operation

### Importance of .cursor Configuration

The `.cursor` folder is **essential** for:
1. **Consistent Code Quality**: Automated enforcement of coding standards
2. **AI Transparency**: Clear visibility of applied development rules
3. **Project Structure**: Organized rule management and application
4. **Development Workflow**: Streamlined AI-assisted development process

**⚠️ Important**: Never modify or delete `.cursor` folder contents without understanding their impact on the development workflow.

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- OpenRouter API account and key
- Internet connection

### Step-by-Step Installation

1. **Clone or Download the Project**
   ```bash
   git clone <repository-url>
   cd Simple-Chat-Bot-Cursor
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

6. **Initialize Cursor Rules (Optional)**
   If using Cursor IDE, run the initialization script:
   ```powershell
   .\initialize_cursor_rules.ps1
   ```

## Usage Instructions

### Running the Chatbot

1. **Ensure Virtual Environment is Active**
   ```bash
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Start the Application**
   ```bash
   python src/chatbot.py
   ```

3. **Interact with the Chatbot**
   - Type your questions and press Enter
   - The AI will respond using the Mistral-7B-Instruct model
   - Type `quit` or `exit` to end the conversation

### Example Interaction
```
Welcome to the Simple Console Chatbot!
Type 'quit' or 'exit' to end the conversation
--------------------------------------------------

You: What is artificial intelligence?
Assistant: Artificial intelligence (AI) refers to the simulation of human intelligence in machines...

You: exit
Goodbye!
```

## Dependencies Detailed Explanation

### Core Dependencies

1. **LangChain (`langchain`)**
   - **Purpose**: Framework for developing applications with language models
   - **Usage**: Provides ChatOpenAI class for OpenRouter API integration
   - **Features**: Message handling, streaming responses, model abstraction
   - **Version**: Latest stable (no fixed version requirement)

2. **Python-dotenv (`python-dotenv`)**
   - **Purpose**: Environment variable management from .env files
   - **Usage**: Securely loads OpenRouter API key from .env file
   - **Security**: Prevents hardcoding sensitive API keys in source code
   - **Best Practice**: Essential for production deployment

3. **Requests (`requests`)**
   - **Purpose**: HTTP library for API communications
   - **Usage**: Handles HTTP requests to OpenRouter API endpoints
   - **Features**: SSL support, request/response handling, error management
   - **Reliability**: Industry-standard HTTP client library

## Troubleshooting

### Common Issues

1. **"Error: OPENROUTER_API_KEY not found"**
   - Solution: Ensure `.env` file exists with correct API key
   - Check: File is in project root directory
   - Verify: API key is valid and active

2. **"Module not found" errors**
   - Solution: Activate virtual environment and reinstall dependencies
   - Command: `pip install -r requirements.txt`

3. **API connection issues**
   - Check: Internet connection is active
   - Verify: OpenRouter API service status
   - Ensure: API key has sufficient credits/usage limits

### Development with Cursor IDE

1. **Rule Application Issues**
   - Ensure `.cursor` folder is intact
   - Run `.\initialize_cursor_rules.ps1` if rules are missing
   - Check Cursor IDE settings for rule activation

2. **Code Standards Enforcement**
   - Cursor will automatically apply coding standards
   - Follow the "Hello, beautiful learner" function requirement
   - Maintain proper docstring and type hint practices

## Project Features

### Technical Highlights

- **Streaming Responses**: Real-time AI response generation
- **Error Handling**: Comprehensive exception management
- **Token Management**: Free tier optimization with 1000 token limit
- **Type Safety**: Full type hints implementation
- **Code Quality**: PEP 8 compliance and documentation standards

### Cursor IDE Integration Benefits

- **Automated Code Quality**: Consistent formatting and standards
- **Rule-Based Development**: Structured approach to code changes
- **Transparency**: Clear visibility of applied development rules
- **Scalability**: Easy addition of new development rules and standards

## Contributing

When contributing to this project:

1. **Use Cursor IDE** for development when possible
2. **Follow the established rules** in `.cursor/rules/`
3. **Maintain documentation** for any new features
4. **Test thoroughly** in console environment
5. **Respect the coding standards** enforced by Cursor rules

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project is designed as an educational example of Cursor IDE integration with AI chatbot development.

## Support

For issues related to:
- **OpenRouter API**: Check OpenRouter documentation
- **Cursor IDE**: Refer to Cursor IDE official documentation
- **LangChain**: Consult LangChain community resources
- **Project-specific issues**: Review the comprehensive documentation above

---

**Note**: This project demonstrates the power of AI-assisted development using Cursor IDE. The `.cursor` configuration ensures consistent, high-quality code generation and maintains development standards across the entire project lifecycle.