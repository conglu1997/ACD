class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love", "style": "Shakespearean sonnet"},
            "2": {"theme": "nature", "style": "haiku"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        style = t["style"]
        return f"""Generate a poem based on the following theme and style:\n\nTheme: {theme}\nStyle: {style}\n\nYour poem should adhere to the conventions of the specified style. A Shakespearean sonnet consists of 14 lines with a specific rhyme scheme (ABABCDCDEFEFGG) and iambic pentameter. A haiku consists of 3 lines with a syllable pattern of 5-7-5.\n\nAfter generating the poem, explain the stylistic choices you made and how they relate to the theme.\n\nSubmit your response in the following format:\n\nPoem:\n[Your poem here]\n\nExplanation:\n[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the conventions of the specified style.",
            "The poem should be thematically relevant.",
            "The explanation should clearly outline the stylistic choices made."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
