class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology", "keyword": "robot"},
            "2": {"theme": "animals", "keyword": "elephant"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a humorous limerick based on the following theme and keyword:

Theme: {t['theme']}
Keyword: {t['keyword']}

A limerick is a five-line poem with a strict rhyme scheme (AABBA) and a specific rhythm. The first, second, and fifth lines should have 7-10 syllables and rhyme with each other, while the third and fourth lines should have 5-7 syllables and rhyme with each other. Ensure that your limerick is humorous and incorporates the given keyword in a meaningful way."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The limerick should include the keyword '{t['keyword']}'.", "The limerick should follow the AABBA rhyme scheme.", "The limerick should adhere to the syllable count requirements.", "The limerick should be humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
