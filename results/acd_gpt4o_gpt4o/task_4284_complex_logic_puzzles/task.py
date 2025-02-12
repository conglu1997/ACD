import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Five people (A, B, C, D, and E) are sitting in a row. A is sitting to the right of B but to the left of C. D is sitting to the left of E but to the right of B. Who is sitting in the middle?"
            },
            "2": {
                "puzzle": "Four friends (W, X, Y, and Z) are at a party. W is not dancing. X is dancing to the left of Z. Y is not dancing to the right of W. Who is dancing to the left of X?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        instructions = f"""Your task is to solve the following logic puzzle:\n\n{puzzle}\n\nProvide your answer in plain text format.\n\nResponse Format:\nAnswer: <Your answer as a single letter, e.g., A, B, C, D, or E>\n\nEnsure your answer is clear and concise."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        correct_answers = {
            "1": "C",
            "2": "Y"
        }
        task_id = "1" if "Five people" in t["puzzle"] else "2"
        return 1.0 if submission.strip().upper() == correct_answers[task_id] else 0.0
