class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": [2, 4, 8, 16, 32]
            },
            "2": {
                "sequence": [1, 1, 2, 3, 5, 8, 13]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the pattern in the following numerical sequence and provide the next three numbers in the sequence:

Sequence: {t['sequence']}

Your response should be a comma-separated list of the next three numbers. Submit your response as a plain text string in the format: 'a, b, c'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should be a comma-separated list of the next three numbers in the sequence."]
        if eval_with_llm_judge(instructions, submission, validation_criteria):
            correct_answers = {
                "1": [64, 128, 256],
                "2": [21, 34, 55]
            }
            task_id = "1" if t['sequence'] == [2, 4, 8, 16, 32] else "2"
            return 1.0 if submission == ', '.join(map(str, correct_answers[task_id])) else 0.0
        return 0.0
