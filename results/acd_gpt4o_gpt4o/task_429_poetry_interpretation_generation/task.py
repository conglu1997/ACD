class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "The sun sets in the west,\nA fiery orb sinking low,\nNight spreads its dark cloak,\nWhispers of stars glow.", "theme": "sunset", "style": "haiku"},
            "2": {"poem": "In the forest deep and dark,\nShadows dance and whispers hark,\nMysteries of the night embark,\nA hidden world, a quiet spark.", "theme": "forest", "style": "rhymed couplets"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        poem = t["poem"]
        theme = t["theme"]
        style = t["style"]
        instructions = f"""Your task involves two parts:\n\n1. Interpretation: Interpret the following poem in terms of its themes, emotions, and stylistic elements:\n\nPoem: {poem}\n\n2. Generation: Create a new poem based on the given theme and style:\n\nTheme: {theme}\nStyle: {style}\n\nYour interpretation should be clear and insightful, addressing the main themes and emotions conveyed by the poem. Your generated poem should adhere to the given theme and style, demonstrating creativity and understanding of poetic form.\n\nResponse Format:\nInterpretation: <Your interpretation>\nGenerated Poem: <Your poem>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should address the main themes, emotions, and stylistic elements of the poem.",
            "The generated poem should adhere to the given theme and style.",
            "The generated poem should demonstrate creativity and understanding of poetic form."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
