# Lab 13 — Multi-Agent NER Crew

## 1. Use case
Мульти-агентна система для NER у слабко структурованих українських парламентських текстах.

---

## 2. Агенти
- Extractor (Stanza NER)
- Reviewer (quality control)
- Fallback (spaCy NER)

---

## 3. Workflow
1. Extractor → первинний NER
2. Reviewer → перевірка результату
3. Якщо потрібно → Fallback
4. Формування FINAL результату

---

## 4. Delegation rules
- Reviewer вирішує чи достатній Extractor output
- fallback активується при:
  - empty output
  - missed entities suspicion

---

## 5. Reviewer
- перевіряє completeness
- перевіряє consistency
- визначає need for fallback

---

## 6. Fallback
- spaCy-based NER
- активується тільки при fail Extractor

---

## 7. Як запускати notebook
Відкрити:
