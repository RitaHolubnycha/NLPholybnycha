
import re

# Регулярки для PII
URL_RE = re.compile(r'https?://\S+|www\.\S+')
EMAIL_RE = re.compile(r'\S+@\S+')
PHONE_RE = re.compile(r'\+?\d[\d\s\-()]{7,}')
MULTISPACE_RE = re.compile(r'\s+')

def clean_text(text: str) -> str:
    text = str(text).replace("\xa0", " ")
    text = MULTISPACE_RE.sub(" ", text)
    return text.strip()

def normalize_text(text: str) -> str:
    text = text.replace("’","'").replace("ʼ","'")
    text = text.replace("—","-")
    text = text.replace("“",'"').replace("”",'"')
    return text

def mask_pii(text: str) -> str:
    text = URL_RE.sub("<URL>", text)
    text = EMAIL_RE.sub("<EMAIL>", text)
    text = PHONE_RE.sub("<PHONE>", text)
    return text

def preprocess(text: str) -> str:
    text = clean_text(text)
    text = normalize_text(text)
    text = mask_pii(text)
    return text
