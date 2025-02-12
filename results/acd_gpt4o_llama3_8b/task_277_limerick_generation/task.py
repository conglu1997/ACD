class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology", "example": "A coder who loved to debug,\nWould sip coffee from a big mug,\nHe fixed every line,\nAnd his code ran just fine,\nBut his social life needed a shrug."},
            "2": {"theme": "fantasy", "example": "A wizard with powers immense,\nCast spells that were highly intense,\nHe turned frogs into kings,\nAnd gave dragons wings,\nHis magic was worth every pence."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        example = t["example"]
        return f"""Generate a limerick based on the following theme: {theme}.

A limerick is a five-line poem with a specific rhyme scheme (AABBA) and a particular rhythm. The first, second, and fifth lines should have 7-10 syllables and rhyme with each other. The third and fourth lines should have 5-7 syllables and rhyme with each other. Ensure your limerick follows this structure and is creative and humorous.

Here is an example limerick on the theme '{theme}':
{example}

Submit your limerick as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The limerick should follow the AABBA rhyme scheme.",
            "The limerick should be creative and humorous.",
            "The limerick should adhere to the theme provided.",
            "The limerick should follow the syllable structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
