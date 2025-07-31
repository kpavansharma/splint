### `backend/dashboard_builder.py`
def build_dashboard_spl(index, sourcetype, source, intent):
    if not (index and sourcetype):
        return "Please provide index and sourcetype to proceed."
    return f"search index={index} sourcetype={sourcetype} {intent} | stats count by host"