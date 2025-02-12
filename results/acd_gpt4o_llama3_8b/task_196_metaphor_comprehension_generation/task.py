class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "metaphor": "Time is a thief that steals our moments.",
                "theme": "love"
            },
            "2": {
                "metaphor": "The world is a stage, and we are merely players.",
                "theme": "freedom"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given metaphor and generate a new metaphor based on the specified theme.

Metaphor: {t['metaphor']}
Theme: {t['theme']}

Your response should include:
1. An interpretation of the given metaphor, explaining its meaning and implications.
2. A new metaphor based on the specified theme.

Example response format:
- Interpretation: The metaphor 'Time is a thief that steals our moments' suggests that time passes quickly and often unnoticed, robbing us of experiences and opportunities without our realization.
- New Metaphor: Love is a fire that warms but can also burn.

Ensure your interpretation is clear and insightful, and your newly generated metaphor is creative and relevant to the theme. Submit your response as a plain text string in the following format:
- Interpretation: [Your interpretation here]
- New Metaphor: [Your new metaphor here]

Make sure to follow the specified format exactly and provide a comprehensive interpretation. Do not reuse the metaphor provided in the task or any common metaphors."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should accurately capture the meaning of the given metaphor.",
            "The new metaphor should be creative and relevant to the specified theme.",
            "The response should follow the specified format precisely.",
            "The interpretation should be clear and insightful.",
            "The new metaphor should demonstrate creativity and cultural relevance.",
            "The new metaphor should not be a common or well-known metaphor.",
            "The new metaphor should not reuse the provided metaphor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
