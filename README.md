# Splint - Splunk + Intelligence — Natural language agent for Splunk dashboards, SPL, and TAs

## ✅ Features
- 🔍 **Dashboard Builder**: Converts natural language to SPL & auto-generates dashboards (asks for index/sourcetype/source first)
- 🏗️ **App/TA Builder**: Interactive agent to build `inputs.conf`, `props.conf`, `transforms.conf` via chat
- 🧠 **SPL Explainer + Runner**: Explains and runs SPL, displays live results
- 🧩 **LLM Router**: Local LLM by default (e.g. Mistral via Ollama), GPT-4 fallback if needed
- 🧠 **Session Memory**: Tracks recent user prompts per session for contextual responses
- 📊 **Feedback Logger**: Captures user feedback for retraining/fine-tuning

---

## 🧠 LLM Support
- Local LLM: Recommended [Mistral-7B-Instruct](https://ollama.com/library/mistral)
- Fallback: GPT-4 (via OpenAI API)
- Uses context routing: if local lacks confidence, switches to GPT-4 (and vice versa)

---

## 🛠️ Requirements
```bash
python>=3.10
fastapi
uvicorn
jinja2
httpx
ollama
openai
splunk-sdk
python-dotenv
```

---

## 🚀 Running the App
```bash
# Step 1: Start Ollama locally with a model
ollama run mistral

# Step 2: Configure API keys in .env (OpenAI, Splunk creds)
OPENAI_API_KEY=sk-...
SPLUNK_HOST=https://splunk-host:8089
SPLUNK_USERNAME=admin
SPLUNK_PASSWORD=changeme

# Step 3: Launch FastAPI server
cd backend
uvicorn main:app --reload

# Step 4: Access chatbot
Open http://localhost:8000/chat
```

---

## 🔁 Training Dataset
- Feedback saved in `data/feedback.jsonl`
- Can be converted to Alpaca format for fine-tuning via LLaMA Factory

---

## 📌 Next Steps
- 🔧 Full Splunk API-based log sampling (dynamic dashboards)
- 🎛️ UI-driven visual builder (drag-drop panels, TA wizard)
- 📈 Analytics dashboard (usage stats, failed queries, routing decisions)
- 🔐 RBAC for enterprise Splunk roles

---
