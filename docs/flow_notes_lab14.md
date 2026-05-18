
# Flow Notes — ЛР14 (Stateful NLP Flow)

## 1. Use case
Структурований NLP pipeline для обробки фінансових, CV та загальних текстових запитів.

## 2. Flow stages
ingest → route → execute → validate → export

## 3. State structure
case_id, raw_text, clean_text, route, execute_output, validation, export, timestamps, warnings, errors

## 4. Routes
- finance_extraction
- cv_extraction
- generic_extraction
- fallback_manual_review

## 5. Execute
Виконує NLP extraction (LLM + rule-based heuristics) відповідно до route.

## 6. Validate
Перевіряє:
- schema correctness
- required fields
- consistency з input
- completeness output

## 7. Fallback
Спрацьовує якщо:
- missing required fields
- invalid schema
- unknown route
- low confidence output

## 8. Export
Structured JSON output для кожного case.

## 9. Improvement vs ad-hoc pipeline
- чіткий контроль етапів
- легкий debugging
- видимі помилки на validation stage

## 10. Overhead
- більше коду ніж simple pipeline
- іноді зайвий route для простих кейсів

## 11. Future improvements
- better routing model
- automatic schema repair
- smarter fallback logic

Generated: 2026-05-18 15:08:35.885964
