# IE Policy

**Типи полів для витягу:**  
1. DATE — дати (формат YYYY-MM-DD)  
2. AMOUNT — суми (float + валюта)  
3. DOC_ID — номер документа (№123/45)

**Правила та словники:**  
- DATE: regex на DD місяць YYYY  
- AMOUNT: regex на числа + валюта, словник валют  
- DOC_ID: regex на '№' + цифри

**Нормалізація:**  
- DATE → YYYY-MM-DD  
- AMOUNT → value + валюта  
- DOC_ID → value як raw string

**Edge cases:**  
- некоректні формати дати  
- '100%' не вважаємо AMOUNT  
- документи без '№' ігноруємо