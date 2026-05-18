def route(state: dict):
    text = state["clean_text"].lower()

    if any(x in text for x in ["грн", "переказ", "monobank"]):
        state["route"] = "finance_extraction"
        state["route_reason"] = "detected money transfer intent"

    elif any(x in text for x in ["cv", "skills", "experience", "python"]):
        state["route"] = "cv_extraction"
        state["route_reason"] = "detected CV / skills context"

    else:
        state["route"] = "generic_summary"
        state["route_reason"] = "no structured pattern detected"

    return state
