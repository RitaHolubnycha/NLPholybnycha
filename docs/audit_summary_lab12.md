
# Audit Summary — Lab 12 (Tool-Grounded Single-Agent)

## 1. Use case
Student lab checker

## 2. Agent task
Агент перевіряє студентську здачу лабораторної роботи:
- repo exists
- valid release tag
- required files structure

## 3. Tools implemented

### check_required_links(submission)
- Input: submission object
- Output: {repo_exists: bool}
- Purpose: перевірка існування репозиторію

### validate_release_tag(tag)
- Input: string
- Output: {valid_tag: bool}
- Purpose: перевірка тегу

### check_repo_structure(files)
- Input: list of files
- Output: {missing_files, structure_valid}
- Purpose: перевірка структури проєкту

## 4. Tool call strategy
input → repo_check → tag_check → structure_check → final decision

## 5. Metrics

- Tool call success rate: 1.0
- Average tool calls per task: 3.0
- Correct answers: 5 / 20

## 6. Baseline vs Agent

Baseline:
- без структурованих перевірок
- можливі помилки інтерпретації

Agent:
- детерміновані перевірки через tools
- менше галюцинацій
- структурований output

## 7. Key insight

Tool-grounded system = не “розумний чат”, а контрольований pipeline перевірок.
