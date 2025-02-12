class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "A baker talking about their favorite type of bread"},
            "2": {"context": "A scientist discussing their favorite element"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a pun based on the following context:

Context: {t['context']}

Your pun should be witty, funny, and relevant to the given context. Submit your pun as a plain text string in the following format:

Pun: [Your witty pun here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The pun should be witty.", "The pun should be funny.", "The pun should be relevant to the given context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
