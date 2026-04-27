import re

def extract(text):
    return {
        "persons": re.findall(r"[А-ЯІЇЄ][а-яіїє]+ [А-ЯІЇЄ][а-яіїє]+", text),
        "orgs": re.findall(r"(Рада|ВРУ|КМУ|Міністерство|РНБО)", text),
        "locations": re.findall(r"(Україна|Крим|Росія)", text),
        "legal_acts": re.findall(r"(закон|постанова|проєкт)", text),
        "dates": re.findall(r"\b(19|20)\d{2}\b", text)
    }
