class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...", "theme": "contrast and paradox"},
            "2": {"excerpt": "All happy families are alike; each unhappy family is unhappy in its own way.", "theme": "family and individuality"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and critique the following literary excerpt based on the specified theme:

Excerpt: {t["excerpt"]}

Theme: {t["theme"]}

Your analysis should include:
1. An interpretation of the excerpt in relation to the theme.
2. A discussion of the literary elements (e.g., metaphor, symbolism, tone) used in the excerpt.
3. A critique of the effectiveness of the excerpt in conveying the theme.
4. Any additional insights or observations related to the excerpt and theme.

Submit your analysis as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should interpret the excerpt in relation to the theme.",
            "The analysis should discuss literary elements used in the excerpt.",
            "The critique should assess the effectiveness of the excerpt in conveying the theme.",
            "The response should provide additional insights or observations related to the excerpt and theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
