class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "peace"},
            "2": {"musical_piece": "Twinkle Twinkle Little Star"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Compose a short musical piece (4-8 bars) based on the following theme:

Theme: {t['theme']}

Describe the mood and elements you have incorporated to reflect the theme. Provide your response in plain text format, and include the composition in a clear textual representation (e.g., ABC notation or a similar format). Your description should be at least 100 words."""
        else:
            return f"""Analyze the following musical composition:

Piece: {t['musical_piece']}

Your analysis should include the structure, key elements, and any notable features. Explain how these elements contribute to the overall effect of the piece. Provide your response in plain text format, structured with an introduction, body, and conclusion. Your analysis should be at least 200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = [
                "The composition should reflect the given theme.",
                "The description should include the mood and elements incorporated and how they relate to the theme.",
                "The composition should be provided in a clear textual representation.",
                "The description should be at least 100 words."
            ]
        else:
            criteria = [
                "The analysis should be detailed and cover the structure, key elements, and notable features of the composition.",
                "The explanation should discuss how these elements contribute to the overall effect of the piece.",
                "The analysis should be structured with an introduction, body, and conclusion.",
                "The analysis should be at least 200 words."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
