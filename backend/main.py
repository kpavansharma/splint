### `backend/main.py`
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from backend.llm_router import route_prompt
from backend.feedback_logger import log_feedback

app = FastAPI()
templates = Jinja2Templates(directory="../frontend/templates")

@app.get("/chat", response_class=HTMLResponse)
def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat")
async def chat(req: Request):
    body = await req.json()
    prompt = body.get("prompt")
    session_id = body.get("session_id", "default")
    response = await route_prompt(prompt, session_id)
    return JSONResponse({"response": response})

@app.post("/feedback")
async def feedback(req: Request):
    body = await req.json()
    log_feedback(body)
    return JSONResponse({"status": "ok"})