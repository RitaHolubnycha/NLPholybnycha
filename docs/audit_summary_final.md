# Фінальний звіт проєкту

## Назва проєкту
POS-tagging українських політичних текстів (UD Ukrainian-ParlaMint)

## Постановка задачі
Задача полягає у автоматичній класифікації частин мови (POS-tagging) для токенів українських парламентських стенограм.

## Датасет
UD Ukrainian-ParlaMint (Universal Dependencies)
Формат: токени + леми + POS (UPOS)

## Pipeline
data → preprocessing → TF-IDF vectorization → classifier (LogReg / LinearSVC) → evaluation → output labels

## Використані бібліотеки
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Використані моделі
- Logistic Regression (baseline)
- LinearSVC (основна модель)
- TF-IDF (word + char n-grams)

## Оцінювання
- accuracy
- macro-F1
- precision / recall
- confusion matrix
- classification report
- PR-curve (для окремих класів)

## Результати

### Baseline (Logistic Regression)
- Accuracy ≈ 0.81
- Macro-F1 ≈ 0.70

### Final model (LinearSVC + word+char n-grams)
- Accuracy ≈ 0.97
- Macro-F1 ≈ 0.83–0.84

## Аналіз помилок
Основні типи помилок:
- плутанина між схожими POS-класами
- помилки на службових словах
- складні морфологічні форми
- рідкісні токени та іншомовні вставки

## Висновок
LinearSVC з комбінованими TF-IDF ознаками (word + char n-grams) показав найкращу якість для POS-tagging українських політичних текстів.
