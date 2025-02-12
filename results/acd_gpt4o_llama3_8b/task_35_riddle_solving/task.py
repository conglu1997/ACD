class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
            },
            "2": {
                "riddle": "The more of this there is, the less you see. What is it?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following riddle by providing the correct answer based on the given clues:

Riddle: {t['riddle']}

Submit your answer as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The answer should be a single word or a short phrase that correctly solves the riddle."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
