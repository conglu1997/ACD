class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"country": "Italy", "capital_city": "Rome"},
            "2": {"country": "Ghana", "capital_city": "Accra"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task requires you to return the capital city of the country '{t["country"]}'. What is the capital city of {t["country"]}?"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        return 1.0 if t["capital_city"].lower() == submission.lower() else 0.0
