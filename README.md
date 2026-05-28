# 🤖 Autonomous AI Newsletter Agent

An autonomous multi-step AI agent that researches the latest AI agent news, summarizes articles, critiques content, and generates a professional newsletter automatically.

Built using LangGraph, Gemini, Tavily Search, and Streamlit.

---

# 🚀 Features

* Autonomous AI workflow
* Multi-step reasoning
* LangGraph orchestration
* Tavily web search integration
* Gemini-powered summarization
* Self-reflection / critique loop
* Human-in-the-loop mode
* HTML + Markdown newsletter generation
* Professional Streamlit dashboard
* Real-time agent logs
* Downloadable newsletter output

---

# 🧠 Agent Workflow

```text
Planner Agent
    ↓
Research Agent
    ↓
Summarizer Agent
    ↓
Critique Agent
    ↓
Newsletter Generator
    ↓
Delivery Simulation
```

---

# 🏗️ Project Structure

```text
newsletter-agent/
│
├── app.py
├── main.py
├── requirements.txt
├── .env
│
├── agent/
│   ├── graph.py
│   ├── nodes.py
│   ├── prompts.py
│   └── state.py
│
├── tools/
│   ├── search_tool.py
│   ├── summarize_tool.py
│   ├── review_tool.py
│   └── html_generator.py
│
├── outputs/
│   ├── newsletter.html
│   └── newsletter.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repo-url>
cd newsletter-agent
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

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Keys

Create `.env` file in project root:

```env
GOOGLE_API_KEY=your_gemini_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run Project

```bash
python -m streamlit run app.py
```

---

# 📰 Newsletter Output

Generated files:

* `outputs/newsletter.html`
* `outputs/newsletter.md`

---

# 🛠️ Tech Stack

| Technology | Purpose             |
| ---------- | ------------------- |
| Streamlit  | Frontend UI         |
| LangGraph  | Agent orchestration |
| Gemini     | LLM reasoning       |
| Tavily API | Web search          |
| Jinja2     | HTML rendering      |

---

# 🔍 Autonomous Capabilities

The agent autonomously:

* plans workflow
* researches latest news
* summarizes articles
* critiques newsletter quality
* improves content
* generates final newsletter
* simulates delivery

---

# 🧪 Human-in-the-Loop Mode

Enable approval-based execution for:

* article review
* summary validation
* final newsletter approval

---

# 📸 UI Preview

The application includes:

* professional dashboard
* real-time logs
* critique section
* newsletter preview
* download button

---

# 📈 Future Improvements

* Email integration
* Multi-agent collaboration
* Memory persistence
* Vector database support
* RAG pipeline
* Scheduling automation
* PDF export
* Analytics dashboard

---

# 👨‍💻 Author

Developed as an autonomous AI agent system project using modern LLM orchestration frameworks.
