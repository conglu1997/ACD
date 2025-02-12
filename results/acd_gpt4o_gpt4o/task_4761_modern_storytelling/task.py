class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A chance encounter that changes everything."},
            "2": {"story": "She walked into the coffee shop, unaware that her life was about to change forever. As she ordered her usual latte, she noticed a man sitting in her favorite spot. He was reading a book she loved. Their eyes met, and he smiled. This simple encounter would lead to a series of events that neither could have predicted, forever intertwining their lives."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to write a contemporary short story based on the following theme:

Theme: {t['theme']}

Ensure your story is engaging, coherent, and follows modern storytelling conventions. Include well-developed characters, a clear setting, and a plot with a beginning, middle, and end. Provide your story in plain text format. Your story should be between 300 to 500 words."""
        else:
            return f"""Your task is to analyze the following short story and describe its narrative structure:

Story: {t['story']}

Ensure your analysis includes a discussion of the story's introduction, rising action, climax, falling action, and resolution. Discuss the development of characters, the setting, and how the plot unfolds. Provide your analysis in plain text format. Your analysis should be between 150 to 300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = ["The story should be coherent and engaging.", "The story should follow modern storytelling conventions.", "The story should be relevant to the given theme.", "The story should include well-developed characters, a clear setting, and a structured plot."]
        else:
            criteria = ["The analysis should correctly identify the narrative structure.", "The analysis should discuss the introduction, rising action, climax, falling action, and resolution of the story.", "The analysis should discuss character development, setting, and plot development."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
