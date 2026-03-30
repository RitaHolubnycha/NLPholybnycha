# Lab7 — LinearSVC + Char-ngrams + Imbalance

## 1. Задача
POS tagging (класифікація токенів → UPOS)

## 2. Baseline з ЛР6
TF-IDF word(1,2) + Logistic Regression

Validation:
- Accuracy: 0.8121
- Macro-F1: 0.7082

## 3. Перевірені моделі (ЛР7)

1) LinearSVC + word(1,2)
- Accuracy: 0.8558
- Macro-F1: 0.7447

2) LinearSVC + char(3–5)
- Accuracy: 0.9731
- Macro-F1: 0.8349

3) LinearSVC + char(3–5) + class_weight="balanced"
- Accuracy: 0.9712
- Macro-F1: 0.8364

## 4. Дисбаланс класів
Так, присутній.
Клас PUNCT має значно більшу частоту та спричиняє багато false positive.

## 5. Поріг (threshold)
Поріг підбирався на validation для класу PUNCT.

Обраний поріг:
-1.0001

Логіка:
баланс між precision і recall (зменшення FP для PUNCT без сильного падіння recall)

## 6. Найкраща модель
LinearSVC + char(3–5) + class_weight="balanced"

- Accuracy: 0.9712
- Macro-F1: 0.8364

## 7. Основні помилки

- короткі токени (немає контексту)
- noisy токени (числа, іноземні слова)
- overlap класів (ADJ vs PROPN, NOUN vs PROPN)

## 8. Висновки

- LinearSVC значно перевершує Logistic Regression
- char-ngrams дають найбільший приріст якості
- class_weight="balanced" покращує macro-F1 за рахунок minority класів
- основна проблема — відсутність контексту (token-level задача)

## 9. Що робити далі

- додати контекст (sentence-level features)
- використати word embeddings або трансформери
