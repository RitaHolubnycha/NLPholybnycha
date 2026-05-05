def extractor(text):
    doc = nlp_stanza(text)

    persons, orgs, locations, dates = [], [], [], []

    # =========================
    # 1. STANZA NER
    # =========================
    for ent in doc.ents:
        value = ent.text.strip()
        label = ent.type

        if len(value) < 2:
            continue

        if label == "PER":
            persons.append(value)

        elif label == "ORG":
            orgs.append(value)

        elif label in ["LOC", "GPE"]:
            locations.append(value)

        elif label in ["DATE", "TIME"]:
            dates.append(value)

    text_lower = text.lower()

    # =========================
    # 2. RULES LAYER (correct + enrich)
    # =========================

    # RULE A: multi-word PERSON detection (weak heuristic)
    pattern_person = r"\b[А-ЯІЇЄ][а-яіїє']+\s[А-ЯІЇЄ][а-яіїє']+\b"
    for match in re.findall(pattern_person, text):
        if match not in persons:
            persons.append(match)

    # RULE B: dates like "23 жовтень"
    months = "січень|лютий|березень|квітень|травень|червень|липень|серпень|вересень|жовтень|листопад|грудень"
    pattern_date = rf"\b\d{{1,2}}\s({months})\b"

    for m in re.findall(pattern_date, text_lower):
        dates.append(m[0] if isinstance(m, tuple) else m)

    # RULE C: years
    years = re.findall(r"\b(19|20)\d{2}\b", text)
    for y in years:
        dates.append(y)

    # RULE D: parliamentary org correction (soft rule, not hardcode)
    if "верховний" in text_lower and "рада" in text_lower:
        if not any("рада" in o.lower() for o in orgs):
            orgs.append("Верховна Рада України")

    # RULE E: Ukraine normalization (only if not already present)
    if "україна" in text_lower:
        if not any("україн" in l.lower() for l in locations):
            locations.append("Україна")

    # RULE F: cleanup function
    def clean(lst):
        return list(set([x.strip() for x in lst if x and len(x.strip()) > 1]))

    return {
        "persons": clean(persons),
        "orgs": clean(orgs),
        "locations": clean(locations),
        "legal_acts": [],
        "dates": clean(dates)
    }
