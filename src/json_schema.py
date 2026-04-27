schema = {
    "type": "object",
    "properties": {
        "persons": {"type": "array", "items": {"type": "string"}},
        "orgs": {"type": "array", "items": {"type": "string"}},
        "locations": {"type": "array", "items": {"type": "string"}},
        "legal_acts": {"type": "array", "items": {"type": "string"}},
        "dates": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["persons", "orgs", "locations", "legal_acts", "dates"]
}
