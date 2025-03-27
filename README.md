# AI Research Assistant using LangChain, LangGraph, LangSmith, RAG and MCP (Model Context Protocol)

## Project Description
A research assistant that breaks a topic into subtopics, assigns research to agents, summarizes findings, and compiles a report.

## Features

- Graph-based agent orchestration with **LangGraph**
- Reproducible tracing with **LangSmith**
- Modular agent design for research tasks 
    - **Planner Agent:** Breaks the topic into subtopics.
    - **Researcher Agent**: Gathers info for each subtopic.
    - **Summarizer Agent**: Summarizes and organizes into a report.
- Cache agent responses using **SQLite**
- Contextual document retrieval using **RAG** and **ChromaDB**
- Prompt & context management using **MCP**

## Project Structure

```bash
.
├── agents/               # LLM agents (e.g. researcher, reviewer)
├── config/               # Configurations
├── db/                   # SQLite store
├── graphs/               # LangGraph workflow 
├── mcp/                  # Model Context Protocol (MCP) implementation
├── nodes/                # LangGraph nodes
│     └── conditions      # nodes conditions
├── rag/                  # RAG (retrieval-augmented generation) logic
├── state/                # Shared state classes for LangGraph workflows
├── tests/                # LangGraph test
├── .env.example          # Sample environment variables
├── .gitignore            
├── Makefile              # Task runner
├── requirements.txt      # Python dependencies
└── README.md             
```

## Requirements

- Python=3.11.11
- Virtual environment (recommended)
- `make` (optional)

## To run the project

### Step 1:

#### Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate     
# On Windows: .venv\Scripts\activate 
```

### Step 2:

#### Option 1: Using Makefile

```bash
make setup
```

#### Option 2: Without Makefile

```bash
pip install -r requirements.txt
```

### Step 3:

Copy the `.env.example` file and rename the file to `.env`

### Step 4:

Add API keys to `.env`.

| Key                 | Description                            | Link to Get Key |
|---------------------|----------------------------------------|-----------------|
| `TOGETHER_API_KEY`  | Used for Together AI model access      | [together](https://api.together.xyz/settings/api-keys) |
| `LANGCHAIN_API_KEY` | Used for LangSmith tracing/debugging   | [langsmith](https://smith.langchain.com/) |
| `SEARCHAPI_API_KEY` | Used for search results in RAG         | [searchapi](https://www.searchapi.io/api_tokens) |

## Usage

### Step 1:

To run the MCP development server

#### Option 1: Using Makefile

```bash
make run-mcp
```

#### Option 2: Without Makefile

```bash
mcp dev mcp/server.py
```

### Step 2:

- Visit `http://localhost:5173` to the browser.
- Change the **Command** to `python`
- Change **Arguments** to `mcp/server.py`
- Click to **Connect** and wait for connection
- After establishing the connection, click **Tools** -> **List Tools** -> **research**
- Then write the research topic and **Run Tool**

## To Test Graph Workflow

```bash
make test-graph # with make
python tests/test_graph.py # without make
```