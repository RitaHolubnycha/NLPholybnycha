def reviewer(text, extraction):

    has_any = any(len(v) > 0 for v in extraction.values())

    issues = []

    if not has_any:
        return {
            "verdict": "bad",
            "issues": ["empty_output"],
            "needs_fallback": True
        }

    # soft check: potential missed entities
    if len(text.split()) > 8 and not has_any:
        issues.append("missed_entities_possible")

    # partial ok case
    if has_any:
        return {
            "verdict": "ok",
            "issues": issues,
            "needs_fallback": False
        }

    return {
        "verdict": "bad",
        "issues": issues,
        "needs_fallback": True
    }
