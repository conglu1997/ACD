class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "What is the next number in the sequence: 2, 6, 12, 20, 30, ...?"},
            "2": {"puzzle": "Solve for x in the equation: 3x + 5 = 20. What is the value of x?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following mathematical puzzle: {t['puzzle']}\nSubmit your answer as a single number."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be a single number.", "The response should correctly solve the puzzle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
