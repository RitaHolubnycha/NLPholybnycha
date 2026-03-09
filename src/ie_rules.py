import re

months_ua = ["січня","лютого","березня","квітня","травня","червня",
             "липня","серпня","вересня","жовтня","листопада","грудня"]

currencies = {
    "UAH": ["грн","₴","UAH"],
    "USD": ["$","USD"],
    "EUR": ["€","EUR"]
}

def extract_dates(text):
    results=[]
    date_regex = r"(\d{1,2})[\.\-/ ]?(січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)[\.\-/ ]?(\d{4})"
    for m in re.finditer(date_regex,text):
        day, month, year = m.groups()
        month_idx = months_ua.index(month)+1
        norm = f"{year}-{month_idx:02d}-{int(day):02d}"
        results.append({"field_type":"DATE","value":norm,"start_char":m.start(),"end_char":m.end(),"method":"regex_date"})
    return results

def extract_amounts(text):
    results=[]
    amount_regex = r"(\d[\d\s]*)(грн|\$|USD|EUR|€|₴|UAH)"
    for m in re.finditer(amount_regex,text):
        val, cur = m.groups()
        val = float(val.replace(" ",""))
        cur_norm = None
        for k,v in currencies.items():
            if cur in v:
                cur_norm=k
        results.append({"field_type":"AMOUNT","value":f"{val} {cur_norm if cur_norm else cur}","start_char":m.start(),"end_char":m.end(),"method":"regex_amount"})
    return results

def extract_doc_ids(text):
    results=[]
    doc_regex = r"№\s*\d+(/\d+)?"
    for m in re.finditer(doc_regex,text):
        results.append({"field_type":"DOC_ID","value":m.group(),"start_char":m.start(),"end_char":m.end(),"method":"regex_docid"})
    return results

def extract_all(text):
    return extract_dates(text)+extract_amounts(text)+extract_doc_ids(text)