# Error Analysis (Аналіз помилок)

## Загальний опис
Було проведено аналіз помилок POS-моделі на тестовому наборі UD Ukrainian-ParlaMint на основі confusion matrix та вибірки неправильних передбачень.

---

##  Загальна кількість помилок
Кількість помилкових передбачень: ~1950

---

##  Основні типи помилок

### 1. Плутанина між схожими POS-класами
- ADJ ↔ NOUN
- ADV ↔ INTJ
- PROPN ↔ NOUN

---

### 2. Помилки на числах та символах
- NUM ↔ ADJ
- токени з цифрами часто класифікуються некоректно

---

### 3. Помилки на службових словах
- PART ↔ CCONJ
- AUX ↔ VERB
- іноді CCONJ ↔ PUNCT

---

### 4. Рідкісні та іншомовні токени
- клас X
- запозичені слова

---

##  Конкретні приклади помилок

### Приклад 1
- Sentence: ParlaMint-UA_2022-01-25-m0.u160.p1.lang1.s2  
- Token: 3  
- Gold: ADJ  
- Pred: NUM  

---

### Приклад 2
- Sentence: ParlaMint-UA_2022-01-25-m0.u92.p2.lang1.s4  
- Token: так  
- Gold: ADV  
- Pred: INTJ  

---

### Приклад 3
- Sentence: ParlaMint-UA_2022-01-25-m0.u110.p2.lang1.s4  
- Token: Туреччини  
- Gold: PROPN  
- Pred: NOUN  

---

### Приклад 4
- Sentence: ParlaMint-UA_2022-01-25-m0.u112.p1.lang1.s2  
- Token: 6199  
- Gold: NUM  
- Pred: ADJ  

---

### Приклад 5
- Sentence: ParlaMint-UA_2022-01-25-m0.u99.p12.lang1.s2  
- Token: Будемо  
- Gold: VERB  
- Pred: AUX  

---

### Приклад 6
- Sentence: ParlaMint-UA_2022-01-25-m0.u115.p1.lang1.s1  
- Token: головуючий  
- Gold: ADJ  
- Pred: NOUN  

---

### Приклад 7
- Sentence: ParlaMint-UA_2022-01-25-m0.u116.p1.lang1.s1  
- Token: Забродському  
- Gold: PROPN  
- Pred: ADJ  

---

### Приклад 8
- Sentence: ParlaMint-UA_2022-01-25-m0.u143.p2.lang1.s7  
- Token: книгорозповсюджувачам  
- Gold: NOUN  
- Pred: PROPN  

---

### Приклад 9
- Sentence: ParlaMint-UA_2022-01-25-m0.u172.p4.lang1.s5  
- Token: position  
- Gold: X  
- Pred: NOUN  

---

### Приклад 10
- Sentence: ParlaMint-UA_2022-01-25-m0.u106.p2.lang1.s6  
- Token: і  
- Gold: PART  
- Pred: CCONJ  

---

##  Висновки

- Найбільше помилок виникає між схожими POS-класами
- Службові частини мови (PART / CCONJ / AUX) є найбільш проблемними
- Числа та нетипові токени часто класифікуються неправильно
- Рідкісні та іншомовні токени мають найнижчу стабільність

---

##  Загальний висновок
Модель показує хороші результати на основних класах, але має труднощі з:
- морфологічно складними токенами
- службовими словами
- рідкісними класами
