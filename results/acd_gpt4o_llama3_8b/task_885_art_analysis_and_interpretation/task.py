class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A painting depicting a group of people in Renaissance attire gathered around a table, with elaborate architectural elements in the background. The use of light and shadow is striking, and the expressions on the faces of the individuals range from solemn to joyful.",
                "art_period": "Renaissance"
            },
            "2": {
                "description": "A modern abstract painting with bold, sweeping brushstrokes in vibrant colors. The composition is dynamic, with intersecting lines and shapes creating a sense of movement and energy.",
                "art_period": "Modern"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and interpret the following description of a visual art piece. Your analysis should include:

1. A discussion of the historical context of the art period in which the piece was created.
2. An explanation of the artistic techniques used in the piece.
3. An interpretation of the possible meanings or themes conveyed by the artwork.

Description: {t['description']}

Submit your analysis as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should include a discussion of the historical context.",
            "The analysis should explain the artistic techniques used.",
            "The analysis should provide an interpretation of the possible meanings or themes conveyed by the artwork."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
