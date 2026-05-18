1. Use case

Student lab checker — перевірка здачі лабораторної роботи

2. Agent task

Перевірити submission:

репозиторій
release tag
структуру файлів
3. Tools (мінімум 2)
check_required_links
check_repo_structure
validate_release_tag
4. Як запускати notebook

Відкрити:
notebooks/lab12_tool_grounded_single_agent.ipynb

Запустити:
Run All

5. Де лежать logs

tool_logs_lab12.jsonl

6. Test cases

20 кейсів, що включають:

валідні submission
відсутній repo
неправильний tag
неповні файли
7. Метрики
Tool call success rate: 1.0
Average tool calls per task: 3.0
Correct answers: 5/20
8. Головний висновок

Tool-grounded підхід дозволяє структурувати перевірку submission і зменшує залежність від “інтуїції” LLM, але якість сильно залежить від якості реалізації tools.
