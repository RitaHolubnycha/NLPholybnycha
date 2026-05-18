
# Memory / Knowledge Policy — ЛР14

## 1. State stores
- case_id
- raw_text
- route
- intermediate outputs
- validation results
- final export
- warnings and errors

## 2. Does NOT store
- API keys or credentials
- hallucinated outputs as truth
- irrelevant intermediate steps
- full external documents

## 3. Intermediate outputs
Can be passed between:
ingest → route → execute → validate → export

## 4. Error logging
All errors stored in:
- errors list
- validation issues
- step-level logs

## 5. Knowledge / schema registry
Read-only:
- routing rules
- schema definitions
- regex patterns

## 6. Read-only files
- schema_registry.json
- routing_rules.json

## 7. State pollution prevention
- overwrite only validated outputs
- discard invalid intermediate results

## 8. Restricted data
- no secrets
- no personal sensitive data
- no API keys in logs

Generated: 2026-05-18 15:08:52.962492
