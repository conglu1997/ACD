class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "setup": "Why did the scarecrow win an award?"
            },
            "2": {
                "setup": "Why don't scientists trust atoms?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given the setup for a joke. Your task is to provide a punchline that completes the joke in a humorous and contextually appropriate way.

Joke Setup: {t['setup']}

Note: Ensure that the punchline is original and not a well-known joke. The punchline should be relevant and logically connected to the setup.

Submit your punchline as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The punchline should be humorous.",
            "The punchline should be contextually appropriate for the given setup.",
            "The punchline should be original and not a well-known joke.",
            "The punchline should make logical sense given the setup."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
