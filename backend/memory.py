### `backend/memory.py`

session_memory = {}

def get_memory(session_id):
    return session_memory.get(session_id, [])

def update_memory(session_id, entry):
    if session_id not in session_memory:
        session_memory[session_id] = []
    session_memory[session_id].append(entry)