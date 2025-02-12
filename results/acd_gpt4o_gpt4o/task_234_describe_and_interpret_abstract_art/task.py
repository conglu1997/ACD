class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "chaos and order"},
            "2": {"description": "A canvas dominated by swirling, chaotic lines of dark colors, interspersed with geometric shapes in bright, contrasting hues that seem to impose a sense of structure within the chaos."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to generate a detailed description of an abstract art piece based on the following theme:

Theme: {t['theme']}

Ensure your description is vivid, creative, and captures the essence of the theme. Provide your description in plain text format, with a minimum of 100 words."""
        else:
            return f"""Your task is to interpret the following description of an abstract art piece and explain what you think the artist was trying to convey:

Description: {t['description']}

Ensure your interpretation includes an analysis of the elements mentioned in the description and how they contribute to the overall theme. Provide your interpretation in plain text format, with a minimum of 100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = ["The description should be vivid and creative.", "The description should capture the essence of the given theme.", "The description should be at least 100 words long."]
        else:
            criteria = ["The interpretation should analyze the elements in the description.", "The interpretation should explain how the elements contribute to the overall theme.", "The interpretation should be at least 100 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
