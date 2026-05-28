# POS-tagging українських політичних текстів (UD Ukrainian-ParlaMint)

## Опис проєкту
Цей проєкт реалізує задачу автоматичного визначення частин мови (POS-tagging) для українських політичних текстів на основі корпусу UD Ukrainian-ParlaMint.

Було реалізовано та порівняно кілька класичних ML-моделей із використанням TF-IDF ознак.

---

## Використані дані
- UD Ukrainian-ParlaMint (Universal Dependencies)
- Дані містять токени, леми та POS-мітки (UPOS)
- Train / Validation / Test split

---

## Моделі
- Logistic Regression (baseline)
- LinearSVC (основна модель)
- TF-IDF (word n-grams + char n-grams)

---

## ⚙️ Pipeline
data → preprocessing → TF-IDF → model training → evaluation → prediction

---

## Метрики
- Accuracy
- Macro-F1
- Precision / Recall
- Confusion Matrix
- Classification Report
- PR-curve (для окремих класів)

---

##  Як запустити проєкт

### 1. Відкрити Google Colab
Запустіть ноутбук у Google Colab.

### 2. Завантажити дані
У відповідній клітинці виконати upload файлів:
```python
from google.colab import files
uploaded = files.upload()
