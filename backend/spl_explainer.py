### `backend/spl_explainer.py`
```python
from backend.splunk_client import run_spl_query

def explain_spl(query):
    return f"This SPL runs a search for: `{query}`. It returns events and applies the stats command."

def execute_spl(query):
    return run_spl_query(query)