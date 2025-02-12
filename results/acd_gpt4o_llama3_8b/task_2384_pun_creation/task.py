class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"word": "bicycle"},
            "2": {"word": "calendar"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        word = t["word"]
        return f"""Generate a pun based on the following word: {word}.\n\nYour pun should be humorous and make clever use of the word or its meaning. Ensure your pun is original, contextually appropriate, and demonstrates creativity in wordplay.\n\nSubmit your pun as a plain text string in the following format:\n\nPun: [Your pun here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The pun should be humorous.",
            "The pun should make clever use of the given word or its meaning.",
            "The pun should be original and contextually appropriate.",
            "The pun should demonstrate creativity in wordplay."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
