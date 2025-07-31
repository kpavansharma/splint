### `backend/llm_router.py`
from models.local_llm_runner import ask_local
from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def route_prompt(prompt, session_id):
    local_response = await ask_local(prompt)
    if "don't know" in local_response.lower():
        print("[Routing] Fallback to GPT-4")
        gpt_resp = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return gpt_resp.choices[0].message.content.strip()
    return local_response