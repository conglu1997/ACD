class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": [2, 4, 8, 16], "next_element": 32},
            "2": {"sequence": [1, 4, 9, 16], "next_element": 25},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task requires you to infer the next element in the given logical sequence based on the provided pattern. Here is the sequence: {t["sequence"]}. What is the next element? Provide your answer as a single integer."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        try:
            return 1.0 if int(submission) == t["next_element"] else 0.0
        except ValueError:
            return 0.0
