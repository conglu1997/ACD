class TaskFamily:
    from typing import Optional

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pattern": [
                    [1, 0, 0, 1],
                    [0, 1, 1, 0],
                    [1, 0, 0, 1],
                    [0, 1, 1, 0]
                ],
                "rule": "Each row and column must contain exactly two '1's and two '0's."
            },
            "2": {
                "pattern": [
                    [1, 0, 1],
                    [0, 1, 0],
                    [1, 0, 1]
                ],
                "rule": "Create a 4x4 pattern following the same rule as the given 3x3 pattern."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "rule" in t and "pattern" in t:
            pattern_str = '\n'.join([' '.join(map(str, row)) for row in t['pattern']])
            return f"Solve the following visual pattern puzzle based on the given rule:\n\nPattern:\n{pattern_str}\n\nRule:\n{t['rule']}\n\nSubmit your solution as a series of rows, each represented by a list of numbers (e.g., [[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0]])."
        elif "rule" in t:
            pattern_str = '\n'.join([' '.join(map(str, row)) for row in t['pattern']])
            return f"Create a new visual pattern puzzle based on the given rule and the example pattern:\n\nExample Pattern:\n{pattern_str}\n\nRule:\n{t['rule']}\n\nSubmit your new pattern as a series of rows, each represented by a list of numbers (e.g., [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])."
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "rule" in t and "pattern" in t:
            criteria = [
                "The solution must follow the given rule.",
                "The pattern must be correctly solved based on the rule."
            ]
        else:
            criteria = [
                "The created pattern must follow the given rule.",
                "The new pattern must be a valid 4x4 grid."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
