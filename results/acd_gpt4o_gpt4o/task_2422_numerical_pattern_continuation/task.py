class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": [2, 4, 8, 16, 32], "length": 3},
            "2": {"pattern": [5, 10, 20, 40, 80], "length": 2}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Identify the pattern in the given sequence and provide the next {t['length']} numbers: {t['pattern']}. Format your response as a comma-separated list of numbers."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answers = {
            "1": "64, 128, 256",
            "2": "160, 320"
        }
        task_id = "1" if t['pattern'] == [2, 4, 8, 16, 32] else "2"
        criteria = [f"The continuation should be {correct_answers[task_id]}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
