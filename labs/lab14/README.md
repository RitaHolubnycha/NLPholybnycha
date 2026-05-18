# Lab 14 — Flow Orchestration

## Use case
Stateful NLP flow для обробки текстових запитів (finance / CV / generic).

## Flow steps
ingest → route → execute → validate → fallback → export

## State
Містить:
case_id, raw_text, clean_text, route, execute_output, validation, export, status, errors, warnings, timestamps

## Routes
- finance_extraction
- cv_extraction
- generic_summary

## Validation
Перевіряє required fields для кожного route.

## Fallback
Спрацьовує при невалідному output (missing fields).

## Export
Повертає structured JSON результат.

## Run
```bash
python flow.py
