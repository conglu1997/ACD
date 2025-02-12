class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pattern": "1, 1, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, ...",
                "context": "Continue the given pattern and explain the logic behind it."
            },
            "2": {
                "pattern": "2, 4, 7, 11, 16, 22, 29, 37, ...",
                "context": "Continue the given pattern and explain the logic behind it."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pattern = t["pattern"]
        context = t["context"]
        return f"""Analyze the following pattern: {pattern}.\n\n{context}\n\nYour response should include the continuation of the pattern and a detailed explanation of the logic behind each step in the pattern. Submit your response as a plain text string in the following format: 'Continuation: [Your continuation of the pattern] Explanation: [Your detailed explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The continuation should logically follow the given pattern.", "The explanation should be clear and detailed, accurately describing the logic behind each step of the pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
