
# 📊 Audit Summary — ЛР14 Flow Orchestration

## 1. Use Case
Stateful NLP flow (ingest → route → execute → validate → export)

## 2. Flow stages
- ingest
- route
- execute
- validate
- export

## 3. Test cases
10

## 4. Flow completion rate
1.00

## 5. Validation pass rate
1.00

## 6. Fallback activation rate
0.00

## 7. Export valid rate
1.00

## 8. Manual review / failures
0

---

## 9. Best examples (VALID cases)


- case_id: case_1
  input: sample input 1
  route: finance_extraction

- case_id: case_2
  input: sample input 2
  route: finance_extraction

- case_id: case_3
  input: sample input 3
  route: finance_extraction

## 10. Problematic examples (INVALID cases)


## 11. What flow improved vs ad-hoc pipeline
- clearer debugging via steps
- explicit validation stage
- controlled routing logic
- structured export instead of free text

## 12. What to improve next
- better route classifier
- smarter fallback repair
- reduce false validation failures
- improve normalization (dates, currency)

Generated: 2026-05-18 15:10:05.350684
