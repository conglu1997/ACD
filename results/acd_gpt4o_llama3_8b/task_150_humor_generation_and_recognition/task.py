class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "animals",
                "constraint": "The joke should involve a pun and be appropriate for children."
            },
            "2": {
                "joke_setup": "Why don't scientists trust atoms?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Generate a joke based on the following theme and constraint:

Theme: {t['theme']}
Constraint: {t['constraint']}

Ensure the joke is funny, involves a pun, and is appropriate for children. Submit your joke as a plain text string."""
        else:
            return f"""Complete the following joke by providing an appropriate punchline:

Joke setup: {t['joke_setup']}

Ensure the punchline is funny and fits the setup. Submit your punchline as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if "theme" in t:
            validation_criteria = [
                "The joke should involve a pun.",
                "The joke should be appropriate for children.",
                "The joke should be funny."
            ]
        else:
            validation_criteria = [
                "The punchline should be funny.",
                "The punchline should fit the setup."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
