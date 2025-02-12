class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"limit": 60, "divisor": 8},
            "2": {"limit": 53, "divisor": 5},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Print numbers from 1 to {t["limit"]} (inclusive) divisible by {t["divisor"]}. Give your answer as an array like [5, 10, 20]. The numbers must be in ascending order."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import json

        got = json.loads(submission)
        expected = [i for i in range(1, t["limit"] + 1) if i % t["divisor"] == 0]

        return 1.0 if got == expected else 0.0
