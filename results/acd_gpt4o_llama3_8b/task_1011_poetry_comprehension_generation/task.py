class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;",
                "theme": "choices",
                "structure": "quatrain"
            },
            "2": {
                "poem": "Hope is the thing with feathers\nThat perches in the soul,\nAnd sings the tune without the words,\nAnd never stops at all,",
                "theme": "hope",
                "structure": "quatrain"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given poem and generate a new poem based on the specified theme and structure.

Poem: {t['poem']}

Theme: {t['theme']}
Structure: {t['structure']}

Your response should include:
1. An interpretation of the given poem, explaining its meaning and implications.
2. A new poem based on the specified theme and structure.

Example response format:
- Interpretation: [Your interpretation here]
- New Poem: [Your new poem here]

Ensure your interpretation is clear and insightful, and your newly generated poem is creative, follows the specified theme, and adheres to the specified structure. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should be clear and insightful.",
            "The new poem should follow the specified theme.",
            "The new poem should adhere to the specified structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
