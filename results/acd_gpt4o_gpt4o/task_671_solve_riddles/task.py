class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"},
            "2": {"riddle": "I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following riddle by interpreting its clues and providing an accurate answer.

Riddle: {t['riddle']}

Provide your answer in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The answer should match the correct solution to the riddle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
