# Dataset Card

**Опис:** Датасет текстів українських політичних виступів.

**Лаби:** 1–4  
- ЛР1–2: cleaned & processed_v2  
- ЛР3: додані lemma_text та upos_seq  
- ЛР4: витяг 3 типів полів (DATE, AMOUNT, DOC_ID)

**Структура:**  
- /data/raw — оригінальні тексти  
- /data/processed_v2 — очищені тексти  
- /data/sample — gold subset ЛР4

**PII/Ризики:**  
- телефони, emails, URL замасковані як <PHONE>/<EMAIL>/<URL>  
- витягаються лише дати, суми та номери документів