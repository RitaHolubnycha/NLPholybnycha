def export(state: dict):
    state["export"] = {
        "case_id": state["case_id"],
        "route": state["route"],
        "final_output": state["execute_output"],
        "validation": state["validation"],
        "status": "validated" if state["validation"]["valid"] else "validated_with_warnings"
    }

    state["status"] = "completed"
    return state
