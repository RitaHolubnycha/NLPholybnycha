# Лабораторна робота 5 — Split & Leakage Checks
## Мета
Мета цієї лабораторної роботи — зробити чесний та відтворюваний розподіл даних на train, validation та test, а також перевірити можливі витоки (leakage) у датасеті `processed_v2`.

## Виконані кроки
- Зроблено детермінований розподіл рядків на три спліти за колонкою `split` з пропорціями 80/10/10.
- Перевірено баланс класів між сплітами.
- Виконано перевірку на exact і near duplicates, template та group leakage.
- Збережено спліти у файлах:
  - `data/sample/splits_train_ids.txt`
  - `data/sample/splits_val_ids.txt`
  - `data/sample/splits_test_ids.txt`
- Документація сплітів збережена у `docs/splits_manifest_lab5.json`.
- Підсумковий звіт ризиків — `docs/leakage_risk_report_lab5.md`.
- Короткий аудит сплітів — `docs/audit_summary_lab5.md`.

## Використана стратегія
- Stratified random split за наявним `split` у датасеті.
- Фіксований seed для відтворюваності.
- Контроль балансу класів та уникнення витоків між train/val/test.
