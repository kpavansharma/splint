### `models/local_llm_runner.py`

import subprocess

async def ask_local(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True, text=True
    )
    return result.stdout.strip()