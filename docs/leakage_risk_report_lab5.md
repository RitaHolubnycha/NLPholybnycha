
# Leakage Risk Report — Lab5

Датасет: UD Ukrainian ParlaMint

Стратегія split:
використано офіційний train/dev/test split датасету.

Одиниця split:
sentence_id

Перевірки leakage:

Exact duplicates

train∩test: 39
train∩val: 38
val∩test: 44

Near duplicates:
30

Висновок:
критичних ознак data leakage не виявлено.
