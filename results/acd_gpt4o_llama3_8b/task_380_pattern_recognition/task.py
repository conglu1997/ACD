class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "grid": [
                    ["X", "O", "X", "O"],
                    ["O", "X", "O", "X"],
                    ["X", "O", "X", "O"],
                    ["O", "X", "O", "?"]
                ],
                "task": "Identify the character that should replace the '?' in the grid to complete the pattern."
            },
            "2": {
                "grid": [
                    ["1", "2", "3", "4"],
                    ["2", "3", "4", "5"],
                    ["3", "4", "5", "6"],
                    ["4", "5", "6", "?"]
                ],
                "task": "Identify the character that should replace the '?' in the grid to complete the pattern."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given grid and pattern description. Identify the character that should replace the '?' in the grid to complete the pattern.

Grid:
{chr(10).join([' '.join(row) for row in t['grid']])}

Task: {t['task']}

Submit your answer as a single character.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "1": "X",
            "2": "7"
        }
        task_key = list(TaskFamily.get_tasks().keys())[list(TaskFamily.get_tasks().values()).index(t)]
        correct_answer = correct_answers[task_key]
        criteria = [f"The correct answer should be '{correct_answer}'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
