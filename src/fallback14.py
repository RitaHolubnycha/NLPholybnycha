def fallback(state):
    state["timestamps"]["fallback"] = str(datetime.now())
    issues = state["validation"]["issues"]

    # якщо все ок — нічого не робимо
    if not issues:
        state["fallback_triggered"] = False
        state["fallback_result"] = "no_fallback_needed"
        return state

    state["fallback_triggered"] = True
    state["fallback_result"] = {
        "applied_fixes": [],
        "mode": "rule_based_repair"
    }

    # -------------------------
    # FINANCE FIXES
    # -------------------------
    if state["route"] == "finance_extraction":
        if "missing currency" in issues:
            state["execute_output"]["currency"] = "UAH"
            state["fallback_result"]["applied_fixes"].append("filled_currency_default_UAH")

        if "missing amount" in issues:
            import re
            numbers = re.findall(r"\d+", state["raw_text"])
            if numbers:
                state["execute_output"]["amount"] = int(numbers[0])
                state["fallback_result"]["applied_fixes"].append("recovered_amount_from_text")

    # -------------------------
    # CV FIXES
    # -------------------------
    if state["route"] == "cv_extraction":
        if "missing skills" in issues:
            text = state["clean_text"].lower()
            skills = []
            for skill in ["python", "ml", "sql", "pytorch", "tensorflow"]:
                if skill in text:
                    skills.append(skill)

            state["execute_output"]["skills"] = skills
            state["fallback_result"]["applied_fixes"].append("recovered_skills_keyword_based")

    if not state["fallback_result"]["applied_fixes"]:
        state["status"] = "manual_review"
    else:
        state["status"] = "repaired"

    return state
