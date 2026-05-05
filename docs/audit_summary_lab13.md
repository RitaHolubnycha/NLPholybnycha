
# Audit Summary — Lab 13 (Multi-Agent NER Pipeline)

## 1. Use Case
Multi-agent Named Entity Recognition (NER) system for Ukrainian parliamentary and administrative text.

---

## 2. Agents Implemented
- Stanza Extractor (baseline + main extractor)
- Reviewer Agent (quality control)
- Fallback Agent (spaCy / heuristics)
- Aggregator (final decision logic)

---

## 3. Test Cases
- Total: 40

---

## 4. Valid Final Output Rate
- 0.425

---

## 5. Reviewer Catch Rate
- 0.600

---

## 6. Fallback Activation Rate
- 0.600

---

## 7. Fallback Success Rate
- 0.400

---

## 8. Single-Agent vs Crew Comparison

| Model | Valid Rate |
|------|-----------|
| Baseline | 0.400 |
| Multi-Agent Crew | 0.425 |
| Improvement | 0.025 |

---

## 9. Best Examples


### Example 1
**Input:** верховний рада Україна четвертий скликання
**Output:** ORG: Верховна Рада України, LOC: Україна

### Example 2
**Input:** Добкін Михайло і Резнік Ігор
**Output:** PER: Добкін Михайло, PER: Резнік Ігор

### Example 3
**Input:** на острів Тузла у керченський протока
**Output:** LOC: Тузла

---
### Example 1
**Input:** просити шановний колега підготуватися
**Issue:** no entities extracted

### Example 2
**Input:** розклад засідання
**Issue:** empty output in both systems

### Example 3
**Input:** питання про порядок денний
**Issue:** no named entities


---

## 11. Future Improvements
- Better Ukrainian NER adaptation
- Confidence scoring per entity
- Improved fallback precision
- Per-class metrics (PER/ORG/LOC/DATE)
- Training domain-specific model

---

## Conclusion
Multi-agent pipeline improves robustness compared to single-agent baseline by adding validation and recovery layers.
