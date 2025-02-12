class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "love",
                "rhyme_scheme": "AABB",
                "example": "Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd so are you."
            },
            "2": {
                "theme": "adventure",
                "rhyme_scheme": "ABAB",
                "example": "Over the hills, we roam,\nThrough the valleys, deep and wide,\nSeeking a place to call home,\nWith the stars as our guide."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate lyrics based on the given theme and rhyme scheme. Ensure that your lyrics are creative and adhere to the specified rhyme scheme. Here are the details:

Theme: {t['theme']}
Rhyme Scheme: {t['rhyme_scheme']}

Submit your response as a plain text string in the format:

[Your lyrics]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            f"The lyrics should adhere to the theme '{t['theme']}'.",
            f"The lyrics should follow the rhyme scheme '{t['rhyme_scheme']}'.",
            "The lyrics should be coherent and creative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
