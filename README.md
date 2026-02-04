# AI Operations Assistant

A multi-agent system (Planner, Executor, Verifier) that accepts natural language tasks, performs API calls, and returns structured results. Built for the GenAI Intern Assignment.

## Live Link
**Go here** : https://abhishek2634-truly-madly-main-43cljs.streamlit.app/

## 🏗 Architecture

The system follows a strict multi-agent pipeline:
1.  **Planner Agent**: Uses LLM (`gpt-4o-mini`) to break the user query into a JSON step-by-step plan containing tool selection and arguments.
2.  **Executor Agent**: Deterministic agent that iterates through the plan, mapping tool names to actual Python functions and executing real API calls.
3.  **Verifier Agent**: Aggregates the execution logs and the original query to produce a polished, natural language summary using the LLM.

### Integrated APIs
1.  **GitHub API**: Used to search for repositories (stars, descriptions, URLs).
2.  **Open-Meteo Weather API**: Used to fetch current temperature and wind speed (No API Key required).

## 🚀 Setup & Run Locally

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Abhishek2634/truly_madly.git
    cd truly_madly
    ```

2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    Rename `.env.example` to `.env` and add your OpenAI Key:
    ```bash
    OPENAI_API_KEY=sk-proj-xxxxxxx
    ```

### Running the Application
Run the Streamlit app with one command:
```bash
streamlit run main.py
```

### Some queries you can try 
**Give me weather in Delhi ?**

**Tell me weather in Mumbai and give me top machine learning repo from github ?**

**Give me top AI agents repo from github ?**

