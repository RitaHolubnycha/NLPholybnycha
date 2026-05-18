def validate(state: dict):
    output = state["execute_output"]
    issues = []

    if state["route"] == "finance_extraction":
        if not output.get("amount"):
            issues.append("missing amount")
        if not output.get("currency"):
            issues.append("missing currency")

    if state["route"] == "cv_extraction":
        if not output.get("skills"):
            issues.append("missing skills")

    state["validation"] = {
        "valid": len(issues) == 0,
        "issues": issues,
        "issue_count": len(issues)
    }

    return state
