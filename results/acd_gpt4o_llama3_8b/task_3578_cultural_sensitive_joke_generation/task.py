class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology", "culture": "American"},
            "2": {"theme": "workplace", "culture": "Japanese"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a joke based on the following theme and cultural context. Ensure that the joke is culturally appropriate, humorous, and original.

Theme: {t['theme']}
Culture: {t['culture']}

Submit your response as a plain text string in the following format: 'Joke: [Your joke]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The joke should be culturally appropriate.", "The joke should be humorous.", "The joke should be original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
