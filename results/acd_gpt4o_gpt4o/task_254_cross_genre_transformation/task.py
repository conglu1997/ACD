class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_text": "In a quiet village, the sun set behind the hills as children played in the fields. Suddenly, a loud noise echoed through the valley, startling everyone.", "from_genre": "slice_of_life", "to_genre": "horror"},
            "2": {"original_text": "Captain Aria adjusted the controls as the spaceship neared the asteroid belt. The crew prepared for a routine mining operation.", "from_genre": "science_fiction", "to_genre": "fantasy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to transform the following piece of writing from the {t['from_genre']} genre into the {t['to_genre']} genre. Ensure that you maintain the core narrative elements of the original text while incorporating the conventions and style of the new genre. Include elements unique to the new genre (e.g., supernatural elements for horror, magical elements for fantasy).

Original Text: {t['original_text']}

Your transformed text should be between 150 and 300 words long and should preserve the main storyline and characters from the original."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed text should maintain the core narrative elements of the original.",
            "The transformed text should clearly reflect the conventions and style of the new genre.",
            "The transformed text should include elements unique to the new genre.",
            "The transformed text should preserve the main storyline and characters from the original.",
            "The transformed text should be between 150 and 300 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
