def execute(state: dict):
    text = state["clean_text"]

    if state["route"] == "finance_extraction":
        state["execute_output"] = {
            "amount": 500 if "500" in text else None,
            "currency": "UAH" if "грн" in text else None,
            "product": "Monobank" if "monobank" in text.lower() else None
        }

    elif state["route"] == "cv_extraction":
        state["execute_output"] = {
            "skills": ["python", "ml"] if "python" in text.lower() else []
        }

    else:
        state["execute_output"] = {
            "summary": text[:60]
        }

    return state
