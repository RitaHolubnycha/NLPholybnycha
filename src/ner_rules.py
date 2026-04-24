import re

class NERRules:
    def __init__(self):
        # шаблони для домену парламенту
        self.org_patterns = [
            r"Верховна Рада",
            r"Кабінет Міністрів",
            r"Міністерство [А-ЯІЇЄҐа-яіїєґ]+",
            r"РНБО"
        ]

        self.number_pattern = r"\b\d+([\.,]\d+)?\b"

    def extract(self, text):
        entities = []

        # ORG rules
        for p in self.org_patterns:
            for match in re.findall(p, text):
                entities.append((match, "ORG"))

        # CARDINAL rules
        for match in re.findall(self.number_pattern, text):
            if isinstance(match, tuple):
                match = match[0]
            entities.append((match, "CARDINAL"))

        return entities
