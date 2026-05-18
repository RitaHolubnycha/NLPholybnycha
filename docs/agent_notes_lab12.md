
# Agent Notes — Lab 12 (Tool-Grounded Single-Agent)

## 1. Use case
Student lab checker

## 2. Agent task
Агент перевіряє здачу лабораторної роботи студента:
- перевірка існування репозиторію
- перевірка release tag
- перевірка структури файлів

## 3. Tools implemented
- check_required_links(submission)
- validate_release_tag(tag)
- check_repo_structure(files)

## 4. How agent decides when to call tools
Агент використовує простий rule-based controller:
- якщо є repo_url → виклик check_required_links
- якщо є release_tag → виклик validate_release_tag
- якщо є files → виклик check_repo_structure
Порядок викликів фіксований: repo → tag → structure

## 5. Logging mechanism
Кожен tool call логуються у JSONL файл:
- timestamp
- task_id
- tool_name
- input
- output
- success
- error

Файл: tool_logs_lab12.jsonl

## 6. What tools improved
- зменшили кількість галюцинацій
- забезпечили структуровану перевірку
- підвищили стабільність фінального результату
- зробили результат детермінованим

## 7. Where tools were not helpful
- прості case_1 / case_11 / case_13 / case_20
- коли всі поля вже валідні
- іноді зайві повторні перевірки

## 8. Remaining errors
- інколи missing files визначались частково
- tag validation іноді надто строгий
- agent міг повертати "partly_correct" замість correct

## 9. What would be improved next
- додати smarter routing (LLM-based instead of rules)
- додати retry logic для tool failures
- зменшити redundant tool calls
- покращити normalization file schema checks
