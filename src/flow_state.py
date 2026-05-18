from datetime import datetime

def create_state(case_id: str, text: str):
    return {
        "case_id": case_id,
        "raw_text": text,
        "clean_text": text.strip(),
        "route": None,
        "route_reason": None,
        "execute_output": None,
        "validation": None,
        "export": None,
        "status": "created",
        "errors": [],
        "warnings": [],
        "timestamps": {},
    }
