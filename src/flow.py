from datetime import datetime

from flow_state import create_state
from router import route
from executor import execute
from validator import validate
from fallback import fallback
from exporter import export
from flow_logger import log_step


LOG_PATH = "flow_logs_lab14.jsonl"


def ingest(state):
    state["timestamps"]["ingest"] = str(datetime.now())

    if not state["raw_text"]:
        state["errors"].append("empty input")
        state["status"] = "failed"
        return state

    state["status"] = "ingested"
    return state


def run_flow(case_id: str, text: str):
    state = create_state(case_id, text)

    state = ingest(state)
    log_step(LOG_PATH, {"case_id": case_id, "step": "ingest", "state": state})

    state = route(state)
    state["timestamps"]["route"] = str(datetime.now())
    log_step(LOG_PATH, {"case_id": case_id, "step": "route", "route": state["route"]})

    state = execute(state)
    state["timestamps"]["execute"] = str(datetime.now())
    log_step(LOG_PATH, {"case_id": case_id, "step": "execute", "output": state["execute_output"]})

    state = validate(state)
    state["timestamps"]["validate"] = str(datetime.now())
    log_step(LOG_PATH, {"case_id": case_id, "step": "validate", "validation": state["validation"]})

    state = fallback(state)
    state = export(state)

    state["timestamps"]["export"] = str(datetime.now())
    log_step(LOG_PATH, {"case_id": case_id, "step": "export", "export": state["export"]})

    return state
