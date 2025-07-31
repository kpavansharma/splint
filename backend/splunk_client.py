### `backend/splunk_client.py`

import splunklib.client as client
import splunklib.results as results
import os

def run_spl_query(query):
    service = client.connect(
        host=os.getenv("SPLUNK_HOST"),
        username=os.getenv("SPLUNK_USERNAME"),
        password=os.getenv("SPLUNK_PASSWORD"),
        port=8089
    )
    job = service.jobs.create(query)
    while not job.is_done():
        pass
    return [r for r in results.ResultsReader(job.results())]