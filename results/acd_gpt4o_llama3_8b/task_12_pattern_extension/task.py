class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": "2, 4, 8, 16"},
            "2": {"sequence": "1, 2, 4, 8"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Extend the following sequence by identifying the pattern: {t["sequence"]}. Provide the next two elements in the sequence separated by a comma. For example, if the sequence is '1, 2, 3', you should respond with '4, 5'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        expected_patterns = {
            "2, 4, 8, 16": "32, 64",
            "1, 2, 4, 8": "16, 32",
        }
        return 1.0 if submission.strip() == expected_patterns[t["sequence"]] else 0.0
