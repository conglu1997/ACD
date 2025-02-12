class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "love",
                "genre": "pop"
            },
            "2": {
                "theme": "heartbreak",
                "genre": "country"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate song lyrics based on the given theme and genre:

Theme: {t['theme']}
Genre: {t['genre']}

Ensure the lyrics are coherent, adhere to the conventions of the specified genre, and reflect the given theme. The lyrics should be at least 16 lines long and formatted as a song with verses and a chorus (if applicable). Submit your lyrics as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The lyrics should be coherent and well-structured.",
            "The lyrics should adhere to the conventions of the specified genre.",
            "The lyrics should reflect the given theme.",
            "The lyrics should be at least 16 lines long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
