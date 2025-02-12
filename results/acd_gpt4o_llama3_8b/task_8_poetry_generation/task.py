class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "structure": "haiku"},
            "2": {"theme": "love", "structure": "sonnet"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        structure = t["structure"]
        if structure == "haiku":
            return f"""Generate a haiku (a three-line poem with a 5-7-5 syllable structure) based on the theme of {theme}. Ensure the poem follows the correct syllable count for each line and is meaningful. Submit your poem as a plain text string, with each line separated by a newline character."""
        elif structure == "sonnet":
            return f"""Generate a sonnet (a 14-line poem with a specific rhyme scheme, typically ABABCDCDEFEFGG) based on the theme of {theme}. Ensure the poem follows the correct rhyme scheme and is meaningful. Submit your poem as a plain text string, with each line separated by a newline character."""
        else:
            return "Unsupported structure."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["structure"] == "haiku":
            criteria = ["The poem should have three lines.", "The syllable count should be 5-7-5.", "The poem should be meaningful."]
        elif t["structure"] == "sonnet":
            criteria = ["The poem should have 14 lines.", "The rhyme scheme should be ABABCDCDEFEFGG.", "The poem should be meaningful."]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
