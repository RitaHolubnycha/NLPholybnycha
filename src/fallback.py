def fallback(text):
    doc = nlp_spacy(text)

    result = {
        "persons": [],
        "orgs": [],
        "locations": [],
        "legal_acts": [],
        "dates": []
    }

    for ent in doc.ents:
        if ent.label_ == "PER":
            result["persons"].append(ent.text)
        elif ent.label_ == "ORG":
            result["orgs"].append(ent.text)
        elif ent.label_ == "LOC":
            result["locations"].append(ent.text)
        elif ent.label_ == "DATE":
            result["dates"].append(ent.text)

    return result
