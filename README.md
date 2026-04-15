# AI chatbot agent

> A conversational AI chatbot built with Streamlit and OpenAI's GPT-4o Mini —
> featuring a clean chat UI, session memory, and real-time response streaming.

---

## 🧩 Problem it solves

Building a usable AI chat interface from scratch requires wiring together an LLM
API, managing conversation history, and handling UI state — which is non-trivial.
This project packages all of that into a clean, deployable Streamlit app that
anyone can clone, add their API key to, and run locally or deploy to the web in
minutes.

---

## 🛠️ Technologies used

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web app UI and session state |
| OpenAI API (GPT-4o Mini) | Language model backend |
| dotenv | Secure API key management |

---

## ⚙️ Installation & setup

**1. Clone the repo**
```bash
git clone https://github.com/I-am-keerthana/ChatBot-Agent-Development.git
cd ChatBot-Agent-Development
```

**2. Install dependencies**
```bash
pip install streamlit openai python-dotenv
```

**3. Add your OpenAI API key**

Create a `.env` file in the project root:
insert your apikey

**4. Run the app**
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---



## 📊 Features

- Multi-turn conversation with full session memory
- Real-time streaming responses (no waiting for full reply)
- Clean, minimal chat UI built entirely in Streamlit
- Easy to extend — swap GPT-4o Mini for any OpenAI model in one line

---

