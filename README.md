# 🤖 Day-01 LLM Chatbot

A simple **Large Language Model (LLM) powered chatbot** built as part of my **30 Days GenAI Challenge**.

This project focuses on understanding the fundamentals of building LLM applications, including project architecture, prompt management, configuration handling, LLM integration, and modular Python development.

---

## 📌 Project Overview

Large Language Models have transformed the way applications interact with users by enabling natural language understanding and generation.

In this project, I built a modular chatbot application that communicates with an LLM to generate responses based on user queries.

The project follows a clean application structure by separating:

* Configuration management
* LLM communication logic
* Prompt templates
* Logging
* Application entry point

This structure makes the application easier to maintain and extend for advanced GenAI applications like RAG systems and AI agents.

---

# ✨ Features

* ✅ LLM-powered conversational responses
* ✅ Modular Python project structure
* ✅ Environment variable based configuration
* ✅ Centralized logging system
* ✅ Prompt template management
* ✅ Clean separation of application components
* ✅ Scalable architecture for future GenAI enhancements

---

# 🏗️ Project Architecture

```
User Query
    |
    ↓
main.py
    |
    ↓
Prompt Management
(prompts.py)
    |
    ↓
LLM Interface
(llm.py)
    |
    ↓
Large Language Model
    |
    ↓
Generated Response
```

---

# 📂 Project Structure

```
Day-01-LLM-Chatbot
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── main.py
│   │   └── Application entry point
│   │
│   ├── config.py
│   │   └── Environment and application configuration
│   │
│   ├── llm.py
│   │   └── LLM connection and response generation logic
│   │
│   ├── prompts.py
│   │   └── Prompt templates for chatbot interaction
│   │
│   └── logger.py
│       └── Logging configuration
│
├── README.md
│
├── requirements.txt
│
└── .env
    └── API keys and environment variables
```

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Generative AI

* Large Language Models (LLMs)
* Prompt Engineering
* Context Management

## Frameworks & Libraries

* LangChain
* Python-dotenv
* Logging

## Development Tools

* VS Code
* Git
* GitHub

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/venky9603/Day-01-LLM-Chatbot.git
```

Navigate into the project:

```bash
cd Day-01-LLM-Chatbot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root directory:

```
LLM_API_KEY=your_api_key_here
```

Replace the placeholder with your actual API key.

⚠️ Never upload API keys to GitHub.

---

# ▶️ Running the Application

Run the chatbot:

```bash
python -m app.main
```

The application will start and generate responses from the configured LLM.

---

# 🧠 Concepts Learned

Through this project, I learned:

* How LLM applications are structured
* Connecting applications with LLM APIs
* Writing effective prompts
* Managing environment variables securely
* Building modular Python applications
* Organizing GenAI projects professionally

---

# 🚀 Future Enhancements

Planned improvements:

* Add conversation memory
* Add Streamlit user interface
* Add document-based question answering (RAG)
* Integrate vector databases
* Add chatbot evaluation metrics
* Deploy using Docker and cloud platforms

---

# 📈 Part of 30 Days GenAI Challenge

This project is **Day-01** of my journey to build practical Generative AI applications.

The challenge covers:

* LLM Applications
* Prompt Engineering
* Retrieval Augmented Generation (RAG)
* Agentic AI
* LLMOps
* AI Application Deployment

---

# 👨‍💻 Author

**Venkatesh Maragoni**

Aspiring Generative AI Engineer | LLM Engineer | Agentic AI Developer

GitHub:
https://github.com/venky9603
