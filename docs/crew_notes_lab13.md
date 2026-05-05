# Crew Notes — Lab 13

## 1. Use case
Мульти-агентна система для Named Entity Recognition (NER) у слабко структурованому українському тексті (транскрипти парламентських засідань).

---

## 2. Агенти в crew
- Extractor (Stanza-based NER)
- Reviewer (quality control + consistency check)
- Fallback (spaCy-based backup extractor)

---

## 3. Роль кожного агента

### Extractor
- Основний NER агент
- Використовує Stanza
- Повертає:
  - persons
  - orgs
  - locations
  - legal_acts
  - dates

### Reviewer
- Перевіряє результат Extractor
- Оцінює:
  - чи є порожній результат
  - чи є потенційні пропуски entity
  - чи логічні знайдені сутності
- Приймає рішення:
  - ok → результат фінальний
  - bad → активує fallback

### Fallback
- Використовує spaCy
- Працює як резервний NER
- Повертає додаткові або відсутні сутності

---

## 4. Правила делегування
- Спочатку завжди запускається Extractor
- Reviewer отримує output Extractor
- Якщо:
  - пустий результат
  - або high chance missing entities
  → активується Fallback
- Інакше результат приймається як фінальний

---

## 5. Що перевіряє Reviewer
- empty_output
- missed_entities_possible
- базову семантичну повноту
- чи є хоч одна сутність у ключових полях

---

## 6. Коли спрацьовує fallback
- Extractor повертає порожні поля
- Reviewer ставить verdict = "bad"
- Є ризик пропущених entity

---

## 7. Покращення порівняно зі single-agent
- більше recall (через fallback)
- менше повністю порожніх результатів
- краща стабільність на шумних текстах

---

## 8. Де multi-agent був зайвий
- прості речення без named entities
- короткі службові фрази
- випадки, де Extractor вже достатній

---

## 9. Залишкові помилки
- часткова агрегація назв (напр. "Верховний рада")
- неправильна сегментація імен
- неповні дати (місяць без року)
- інколи дублювання сутностей

---

## 10. Подальші покращення
- додати нормалізацію entity (entity linking)
- покращити tokenizer для української
- додати rule-based postprocessing
- навчити lightweight NER модель під домен парламенту
