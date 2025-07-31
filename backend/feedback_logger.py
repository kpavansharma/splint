### `backend/feedback_logger.py`

import json
from datetime import datetime

def log_feedback(data):
    with open("../data/feedback.jsonl", "a") as f:
        data["timestamp"] = datetime.utcnow().isoformat()
        f.write(json.dumps(data) + "\n")


