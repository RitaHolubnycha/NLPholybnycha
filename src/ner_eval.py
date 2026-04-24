class NEREvaluator:
    def compare(self, baseline, hybrid):
        """
        Просте порівняння:
        - baseline: spaCy entities
        - hybrid: spaCy + rules
        """

        baseline_set = set(baseline)
        hybrid_set = set(hybrid)

        return {
            "baseline_count": len(baseline_set),
            "hybrid_count": len(hybrid_set),
            "added_by_rules": len(hybrid_set - baseline_set),
            "missing_after_hybrid": len(baseline_set - hybrid_set)
        }

    def error_stats(self, results):
        errors = {
            "missed": 0,
            "added": 0,
            "duplicates": 0
        }

        for r in results:
            if len(r["spacy"]) == 0 and len(r["rules"]) > 0:
                errors["added"] += 1

            if len(r["spacy"]) > 0 and len(r["rules"]) == 0:
                errors["missed"] += 1

        return errors
