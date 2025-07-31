### `backend/app_ta_builder.py`

def build_conf_files(data):
    return {
        "inputs.conf": f"[monitor://{data['path']}]
sourcetype={data['sourcetype']}
index={data['index']}\n",
        "props.conf": f"[{data['sourcetype']}]
TRANSFORMS-set=extract_fields\n",
        "transforms.conf": f"[extract_fields]
REGEX=(?<field>\w+)
FORMAT=field::$1
DEST_KEY=queue\n"
    }