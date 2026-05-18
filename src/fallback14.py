def fallback(state: dict):
    if state["validation"]["valid"]:
        return state

    state["warnings"].append("validation_failed -> fallback activated")

    # простий rule-based fallback
    if state["route"] == "finance_extraction":
        if not state["execute_output"].get("amount"):
            state["execute_output"]["amount"] = 0

    return state
